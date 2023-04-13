from django.test import TestCase
from payment.models import Ticket, QrCode, TicketRecieved


class Test_Tickets(TestCase):
    def setUp(self):
        self.ticket1 = Ticket.objects.create(
            name="ticket name", email="email@email.com"
        )

    def test_ticket_is_assigned_id(self):
        self.assertTrue(self.ticket1.id)

    def test_ticket_str_function(self):
        self.assertEquals(str(self.ticket1), self.ticket1.__str__(), self.ticket1.id)

class Test_QRcode(TestCase):
    def setUp(self):
        self.ticket1 = Ticket.objects.create(
            name="ticket name", email="email@email.com"
        )
        self.qr_code = QrCode.objects.create(
            name = "qrcode",
            ticket = self.ticket1

        )
    def test_qrcode_str_function(self):
        self.assertEquals(str(self.qr_code), self.qr_code.__str__(), self.qr_code.name)



class Test_Ticket_Received(TestCase):
    def setUp(self):
        self.ticket1 = TicketRecieved.objects.create(
            name="ticket name", email="email@email.com"
        )
    def test_str_function(self):
        self.assertEquals(str(self.ticket1), self.ticket1.__str__(), self.ticket1.name)
        
