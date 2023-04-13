from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Profile, RegistrationCode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .token_generator import activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import login
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random


def register(request):
    while RegistrationCode.objects.all().count() <= 24:
        generated_code = random.randint(1, 9999999999999999)
        RegistrationCode.objects.create(code=generated_code)

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            current_site = get_current_site(request)
            subject = "Email Verification"
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            registration_code = form.cleaned_data.get("registration_code")

            required_code = RegistrationCode.objects.filter(code=registration_code)

            existed_email = User.objects.filter(email=email).exists()

            if required_code and not existed_email:
                user.is_active = False
                user.save()
                message = render_to_string(
                    "users/email.html",
                    {
                        "username": username,
                        "current_site": current_site,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": activation_token.make_token(user),
                    },
                )
                email_ = EmailMessage(subject, message, to=[email])
                email_.content_subtype = "html"
                email_.send()
                print("done")

                required_code.delete()

                return redirect("Need Verification")

            if existed_email:
                messages.error(request, "This email already exists")
            else:
                messages.error(request, "The Registration Code is invalid")

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form, "title": "Register"})


class UserProfile(DetailView):
    model = User
    template_name = "users/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        context["user"] = self.get_object()
        context["committee"] = self.get_object().profile.committee
       
        return context


class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "users/update_profile.html"
    fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "You have successfully updated your profile")
            return redirect("Profile", username=request.user.username)

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Editting Profile",
    }

    return render(request, "users/update_profile.html", context)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, ObjectDoesNotExist):
        user = None
    if user and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
    else:
        messages.error(
            request, "Activation link is invalid!", {"title": "Verification"}
        )
    return render(request, "users/verify.html")


def need_verify(request):
    return render(request, "users/need_verify.html")
