from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class TicketForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.id}'

class QrCode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    ticket = models.OneToOneField(TicketForm, on_delete=models.SET_NULL, null=True)
    qr_code = models.ImageField(upload_to='qrcodes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        qrcode_img = qrcode.make(self.ticket.email)
        canvas = Image.new('RGB', (340,340), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname , File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Ticket_Recieved(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    code = models.OneToOneField(QrCode , on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.name}'

