from django.core.mail.message import EmailMessage
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from apps.dashboard.models import Report
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    ListView,
)
from apps.base.models import Contact, Subscribe, Videos
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.products.models import Products

import pandas as pd
from .forms import ContactForm, ReportForm
from django.http import Http404, JsonResponse
from .utils import get_report_image, is_ajax , sync_excel
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.edit import FormMixin
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.auth.models import Permission
from apps.users.models import Profile

@login_required
def dashboard(request):
    committee = request.user.profile.committee.name

    context = {"title": f"{committee} | Dashboard"}
    
    if request.user.profile.position not in ["President", "Operations"]:
        if committee == "IT":
            return redirect("/us")

        if committee != "IT":
            template = f"dashboard/{committee}/dashboard.html"

        if committee in ["Coaching", "Media", "Videography", "Design"]:
            raise Http404()
    if request.user.profile.position == "Operations":
        template = "dashboard/Operations/dashboard.html"
    
    return render(request, template, context)


class SubscribersListView(LoginRequiredMixin, ListView):
    model = Subscribe
    context_object_name = "subs"
    template_name = "dashboard/Marketing/subscribers_list.html"
    ordering = ["-date_subscribed"]
    paginate_by = 10


@login_required
def data_frame(request):
    qs = Products.objects.prefetch_related("Products").values()
    data = pd.DataFrame(qs)
    context = {
        "df": data.to_html(classes="products_table thead", index=False),
    }

    return render(request, "dashboard/ER/dataframes.html", context)

@login_required
def sync_to_sheets(request):
    

    return redirect(reverse("dataframes"))



@login_required
def export_to_csv(request):
    if request.method == "POST":
        qs = Products.objects.all().values()
        data = pd.DataFrame(qs)

        response = HttpResponse(content_type="text/csv")

        response["Content-Disposition"] = "attachment; filename=dataframe.csv"

        data.to_csv(path_or_buf=response, float_format="%.2f", index=False, decimal=",")
    else:
        raise Http404()

    return response


class ProductChartView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/ER/datacharts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pt"] = Products.objects.all()
        context["form"] = ReportForm()
        return context


def create_report_view(request):
    form = ReportForm(request.POST)
    print(form)
    if is_ajax(request=request):
        image = request.POST.get("image")
        img = get_report_image(image)
        author = User.objects.get(id=request.user.id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()
        return JsonResponse({"msg": "send"})
    return JsonResponse({})


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = "dashboard/ER/reports.html"
    ordering = ["-created"]


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "dashboard/ER/reports_detail.html"


def render_pdf_view(request, pk):
    template_path = "dashboard/ER/report_pdf.html"
    obj = get_object_or_404(Report, pk=pk)
    context = {"obj": obj}
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Videos
    template_name = "dashboard/Marketing/create_video.html"
    fields = ["name", "urlID"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Videos
    template_name = "dashboard/Marketing/update_video.html"
    fields = ["name", "urlID"]

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.user:
            return True
        return False


class VideoDeleteView(LoginRequiredMixin, DeleteView):
    model = Videos
    template_name = "dashboard/Marketing/delete_video.html"
    success_url = "/watchus"

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.user:
            return True
        return False


class InboxListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "dashboard/HR/inbox.html"
    context_object_name = "Contact"
    ordering = ["-created"]


class InboxDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Contact
    template_name = "dashboard/HR/inbox_detail.html"
    form_class = ContactForm

    def get_success_url(self):
        return reverse("Inbox_Detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        self.object.reply = form.cleaned_data["reply"]
        self.object.save()
        subject = "Replied"
        message = render_to_string(
            "dashboard/HR/reply_email.html",
            {"reply": self.object.reply, "message": self.object.message},
        )
        sending_email = EmailMessage(subject, message, to=[self.object.email])
        sending_email.content_subtype = "html"
        sending_email.send()
        return super().form_valid(form)


def inbox_delete(request, pk):
    form = Contact.objects.get(pk=pk)
    form.delete()
    return render(request, "dashboard/HR/inbox.html")


class AssignMembersList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "dashboard/assign_users.html"
    paginate_by = 10
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.filter(position="Member").exclude(user__is_staff=True)


def give_permission(request):
    permission = Permission.objects.get(codename="can_view_dashboard")
    if request.method == "POST":
        members = request.POST.getlist("member")
        if "perm_btn" in request.POST:
            for member in members:
                user = User.objects.get(id=member)
                user.user_permissions.add(permission)
                user.save()
        if "remove_perm_btn" in request.POST:
            for member in members:
                user = User.objects.get(id=member)
                user.user_permissions.remove(permission)
                user.save()
        if "assign_btn" in request.POST:
            for member in members:
                user = User.objects.get(id=member)
                user.profile.committee = request.user.profile.committee
                user.save()

    return redirect("Assign")

