from django.shortcuts import render, redirect
from django.core.validators import validate_email, ValidationError
from django.contrib.auth.models import User
from apps.users.models import Committee
from django.core.mail import (
    send_mail,
    EmailMessage,
    get_connection,
    EmailMultiAlternatives,
)
from django.contrib import messages
from django.conf import settings
from .models import Videos, Subscribe, Contact, Speakers, ImageSpeakers
from .forms import SubscribeForm, NewsletterForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView
from uuid import uuid4
from apps.users.models import Profile
from apps.dashboard.models import HomePage , AboutPage

def home(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Email Verification"
            email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            token = uuid4()

            message = render_to_string(
                "base/email_verify_subscribe.html",
                {
                    "current_site": current_site,
                    "form_id": user.id,
                    "token": token,
                    "name": name,
                },
            )
            subscribe_email = EmailMessage(subject, message, to=[email])
            subscribe_email.content_subtype = "html"
            subscribe_email.send()

            return redirect("Need Verification")

    else:
        form = SubscribeForm()
    try:
        home_title = HomePage.objects.get(id=1).title
        home_content = HomePage.objects.get(id=1).content
        home_title_2 = HomePage.objects.get(id=1).title_2
        home_content_2 = HomePage.objects.get(id=1).content_2
    except HomePage.DoesNotExist:
        home_title = home_content = home_title_2 = home_content_2 = None

    context = {
        "form": form,
        "home_title": home_title,
        "home_content": home_content,
        "home_title_2": home_title_2,
        "home_content_2": home_content_2,
    }
    return render(request, "base/home.html", context)


def subscribed(request):
    return render(request, "base/subscribed.html")


def subscribe_email(request):
    return render(request, "base/subscribe_email.html")


def unsubscribe(request):
    return render(request, "base/unsubscibe.html")


# Testing Subscribtion EMail
def test_email(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            email = request.user.email
            subject = "News for you"
            message = render_to_string(
                "base/subscribe_email.html",
                {
                    "name": name,
                },
            )
            send_subscribe = EmailMessage(subject, message, to=[email])
            send_subscribe.content_subtype = "html"
            send_subscribe.send()
            return redirect("/complete-subscribe")
    else:
        form = NewsletterForm()

    return render(request, "base/subscribe_form.html", {"form": form})


# Real subscirbition Email
def complete_subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            subject = "News for you"
            message = render_to_string(
                "base/subscribe_email.html",
                {
                    "name": name,
                },
            )
            for users_email in Subscribe.objects.values_list("email", flat=True):
                subs = Subscribe.objects.filter(subscribed=True, email=users_email)
                if subs:
                    connection = (
                        get_connection()
                    )  # uses SMTP server specified in settings.py
                    connection.open()

                    send_subscribe = EmailMultiAlternatives(
                        subject, message, to=[users_email]
                    )
                    send_subscribe.content_subtype = "html"
                    send_subscribe.send()
                    connection.close()
                return redirect("/complete-subscribe")

    else:
        form = NewsletterForm()

    return render(request, "base/subscribe_form.html", {"form": form})


def activate_account(request, pk, token):
    sub = Subscribe.objects.get(pk=pk)
    sub.subscribed = True
    sub.save()
    return render(request, "base/subscribed.html")


def about(request):
    committees = Committee.objects.all()
    for committee in committees:
        if committee.name == "IT":
            committees = [committee] + [
                committee for committee in committees.exclude(id=committee.id)
            ]
    members = Profile.objects.all()
    try:
        about_title = AboutPage.objects.get(id=1).title
        about_content = AboutPage.objects.get(id=1).content
        about_title_2 = AboutPage.objects.get(id=1).title_2
        about_content_2 = AboutPage.objects.get(id=1).content_2
    except AboutPage.DoesNotExist:
        about_title = about_content = about_title_2 = about_content_2 = None
    context = {
        "title": "About",
        "Members": members,
        "Committees": committees,
        "about_title": about_title,
        "about_content": about_content,
        "about_title_2": about_title_2,
        "about_content_2": about_content_2,
    }
    return render(request, "base/about.html", context)


class VideoListView(ListView):
    model = Videos
    template_name = "base/watch-us.html"
    context_object_name = "videos"
    ordering = ["-date_posted"]


def events(request):
    return render(request, "base/events.html", {"title": "Events"})


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        email = request.POST["email"]

        try:
            validate_email(email)
            Contact.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            send_mail(
                subject,
                f"Email: {email}\n\nMessage: {message}",
                "from@example.com",
                [settings.EMAIL_HOST_USER],
            )
            return render(request, "base/contact.html", {"name": name})
        except ValidationError as e:
            messages.error(request, e.message)

    return render(request, "base/contact.html", {"title": "Contact"})


class SpeakersListView(ListView):
    model = Speakers
    template_name = "base/speakers.html"
    context_object_name = "speakers"
    ordering = ["-date_posted"]
    paginate_by = 6

    def get_context_data(self, **kwargs):
        photos = ImageSpeakers.objects.filter(default=True)
        context = {"photos": photos}
        return context


def error_404_view(request, exception=None):
    return render(request, "base/404.html", status=404)


def speakers(request, pk):
    photos = ImageSpeakers.objects.filter(default=True)
    context = {"photos": photos}
    return render(request, "base/speaker.html", context)
