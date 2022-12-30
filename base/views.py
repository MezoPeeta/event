from django.shortcuts import  render,redirect
from django.core.validators import validate_email , ValidationError
from django.core.mail import send_mail , EmailMessage , get_connection , EmailMultiAlternatives
from django.contrib import messages
from django.conf import settings
from .models import Videos , Subscribe , Contact, Speakers
from .forms import Subscribe_Form , Newsletter_Form
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView
from django.core.cache import cache
from uuid import uuid4


def home(request):
    cache.clear()
    if request.method == 'POST':
        
        form = Subscribe_Form(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Email Verification"
            email = form.cleaned_data.get("email")
            token = uuid4()

            message = render_to_string('base/email.html', {
                'current_site': current_site,
                'form_id' : user.id,
                'token' : token,
                })
            subscribe_email = EmailMessage(subject, message, to=[email])
            subscribe_email.content_subtype = 'html'
            subscribe_email.send()

            return redirect('Need Verification')

    else:
        form = Subscribe_Form()
    return render(request, 'base/home.html' , {'form': form})

def subscribed(request):

    return render(request, 'base/subscribed.html')

def subscribe_email(request):
    return render(request, 'base/subscribe_email.html')

def unsubscribe(request):
    return render(request , 'base/unsubscibe.html')

#Testing Subscribtion EMail
def test_email(request):

    if request.method == "POST":
        form = Newsletter_Form(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = request.user.email
            subject = 'News for you'
            message = render_to_string('base/subscribe_email.html', {
                'name' : name,

            })
            send_subscribe = EmailMessage(subject ,message, to=[email])
            send_subscribe.content_subtype = 'html'
            send_subscribe.send()
            return redirect('/complete-subscribe')
    else:
        form = Newsletter_Form()
        
    return render(request, 'base/subscribe_form.html', {'form': form})

#Real subscirbition Email
def complete_subscribe(request):

    if request.method == "POST":
        form = Newsletter_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')  
            subject = 'News for you'
            message = render_to_string('base/subscribe_email.html', {
                'name' : name,
                
            })
            for users_email in Subscribe.objects.values_list("email", flat=True):
                subs = Subscribe.objects.filter(subscribed=True , email = users_email)
                if subs:
                    connection = get_connection() # uses SMTP server specified in settings.py
                    connection.open() 

                    send_subscribe = EmailMultiAlternatives(subject ,message, to=[users_email])
                    send_subscribe.content_subtype = 'html'
                    send_subscribe.send()
                    connection.close()
                return redirect('/complete-subscribe')
            
    else:
        form = Newsletter_Form()
        
    return render(request, 'base/subscribe_form.html', {'form': form})


def activate_account(request, pk,token):
    sub = Subscribe.objects.get(pk=pk)
    sub.subscribed = True
    sub.save()
    return render(request,'base/subscribed.html')

def about(request):
    return render(request, 'base/about.html' ,{'title': 'About'})

def watch_us(request):
    context = {
        'videos' : Videos.objects.all(),
        'title': 'Watch Us'
    }
    return render(request, 'base/watch-us.html', context)

class VideoListView(ListView):
    model = Videos
    template_name = 'base/watch-us.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']



def events(request):

    return render(request, 'base/events.html', {'title': 'Events'})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        try:
            validate_email(email)
            send_mail(
                subject,
                "Email: {}\n\nMessage: {}".format(email, message),
                'from@example.com',
                [settings.EMAIL_HOST_USER],
                 )        
    
        except ValidationError as error:
            messages.error(request, "please enter a valid email")
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        return render(request, 'base/contact.html', {"name": name})
    return render(request, 'base/contact.html', {'title': 'Contact'})

class SpeakersListView(ListView):
    model = Speakers
    template_name = 'base/speakers.html'
    context_object_name = 'speakers'
    ordering = ['-date_posted']
    paginate_by = 6


def error_404_view(request, exception=None):
    return render(request, 'base/404.html',status=404)

