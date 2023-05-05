from django.test import TestCase
from django.urls import reverse
from utils.selenium_test import TestUtils


class TestViews(TestCase, TestUtils):
    def setUp(self):
        self.checkout_url = reverse('CheckOut')
        self.complete_order_url = reverse("Order_Complete")
        self.form_data = {"name":"name","email":"email@email.com"}

    def test_checkout(self):
        response = self.client.get(self.checkout_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payment/checkout.html")

    def test_complete_order(self):
        response = self.client.get(self.complete_order_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "payment/complete_order.html")
    def test_complete_order_post(self):
        response = self.client.post(self.complete_order_url, self.form_data)

        self.assertEquals(response.status_code, 302)



