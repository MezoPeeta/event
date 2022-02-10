from django.shortcuts import render, redirect
import json
from .forms import Ticket_Form , TicketRecieved
from .models import QrCode , TicketForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from products.models import Coupon

def checkout(request):
    if request.method == "POST":
        form = Ticket_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events')
        
                
    form = Ticket_Form()
    return render(request , 'payment/checkout.html', {'form': form})

def complete_order(request):
    if request.method == "POST":
        form = TicketRecieved(request.POST)
        if form.is_valid():
            form.save()

            form_name = form.cleaned_data.get('name')

            form_email = form.cleaned_data.get('email')
            
            qrcode = QrCode.objects.all().get(name = form_name)
            image_link = request.build_absolute_uri(qrcode.qr_code.url)

            subject = 'Ticket'
            message = render_to_string('payment/ticket.html', {
                'name' : form_name,
                'email' : form_email,
                'image': image_link,
            })
            send_ticket = EmailMessage(subject ,message ,to=[form_email])
            send_ticket.content_subtype = 'html'
            send_ticket.send()
            
            return redirect('/complete-order')
    else:
        form = TicketRecieved()
        
    return render(request, 'payment/complete_order.html', {'form': form})

