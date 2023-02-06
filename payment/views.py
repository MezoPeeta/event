from django.shortcuts import render, redirect
from .forms import TicketForm, TicketRecievedForm
# from .models import QrCode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def checkout(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/events")

    form = TicketForm()
    return render(request, "payment/checkout.html", {"form": form})


def complete_order(request):
    if request.method == "POST":
        form = TicketRecievedForm(request.POST)
        if form.is_valid():
            form.save()

            form_name = form.cleaned_data.get("name")

            form_email = form.cleaned_data.get("email")

            # qrcode = QrCode.objects.get(name=form_name)
            # image_link = request.build_absolute_uri(qrcode.qr_code.url)

            subject = "Ticket"
            message = render_to_string(
                "payment/ticket.html",
                {
                    "name": form_name,
                    "email": form_email,
                    # "image": image_link,
                },
            )
            send_ticket = EmailMessage(subject, message, to=[form_email])
            send_ticket.content_subtype = "html"
            send_ticket.send()

            return redirect("/complete-order")
    else:
        form = TicketRecievedForm()

    return render(request, "payment/complete_order.html", {"form": form})
