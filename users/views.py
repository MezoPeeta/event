from django.shortcuts import render , redirect ,HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User 
from django.urls import reverse
from .models import Profile , RegistrationCode
from django.core.mail import send_mail ,EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .token_generator import activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
import random
import pandas as pd
from django.http import HttpResponse
from django.http import Http404

def exportTOCSV(request):
    qs = RegistrationCode.objects.all().values()
    data = pd.DataFrame(qs)

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename=Registration Code.csv'

    data.to_csv(path_or_buf=response, float_format='%.2f',
                index=False, decimal=",")
    

    return response

def register(request):
    
    while RegistrationCode.objects.all().count() <= 24:
        generated_code = random.randint(1,9999999999999999)
        add_code = RegistrationCode.objects.create(code = generated_code)
            
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            current_site = get_current_site(request)
            subject = "Email Verification"
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            registration_code = form.cleaned_data.get("registration_code")
            
            required_code = RegistrationCode.objects.filter(code = registration_code)
            
            existedEmail = User.objects.filter(email = email).exists()
            
            if required_code and existedEmail == False:
                user.is_active = False
                user.save()
                message = render_to_string('users/email.html', {
                'username': username,
                'current_site': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': activation_token.make_token(user)
                })
                email = EmailMessage(subject, message,to=[email])
                email.content_subtype = 'html'
                email.send()
                
                required_code.delete()
                
                return redirect('Need Verification')

                
            elif existedEmail:
                messages.error(request, "This email already exists")
            else:
                messages.error(request, "The Registration Code is invalid")

    else:
        form = UserRegisterForm()

    return render(request , 'users/register.html', {'form': form, 'title': 'Register'})


class UserProfile(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = 'user'
    slug_field = "username"
    slug_url_kwarg = 'username'
    
class UpdateProfile(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['image','bio','committee','position','awards','experience', 'achievement']
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
    for userp in User.objects.all():
        try:
            u = userp.profile
        except ObjectDoesNotExist:
            u = Profile.objects.create(user=userp)


    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, 
            request.FILES,
            instance=request.user.profile,
            )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"You have successfully updated your profile")
            return redirect('Profile' , username = request.user.username)

        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title' : 'Editting Profile'
        }

    return render(request, 'users/update_profile.html', context)

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, ObjectDoesNotExist):
        user = None
    if user and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'users/verify.html')
    else:
        messages.error(request , 'Activation link is invalid!', {'title': 'Verification'})


def needVerify(request):
    return render(request, 'users/need_verify.html')

