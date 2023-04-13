from django.test import TestCase
from base.forms import SubscribeForm
from django.urls import reverse
from utils.selenium_test import TestUtils
from base.models import Subscribe
from uuid import uuid4
from django.core import mail

class TestSubscribe(TestCase, TestUtils):
    def test_subscribe_form(self):
        response = self.client.post(
            reverse("Home"), {"name": "test", "email": "test@gmail.com"}
        )
        self.assertRedirects(response, reverse("Need Verification"))
        mail.send_mail(
            "Email Verification",
            "test",
            "from@gmail.com",
            ["test@gmail.com"],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, "Email Verification")
        form_invalid = SubscribeForm({"name": "test", "email": "test"})
        self.assertFalse(form_invalid.is_valid())
        self.assertEqual(form_invalid.errors["email"], ["Enter a valid email address."])

    def test_subscribe_templates(self):
        response = self.client.get(reverse("Subscribed"))
        self.assertTemplateUsed(response, "base/subscribed.html")
        response = self.client.get(reverse("Subscirbe_Email"))
        self.assertTemplateUsed(response, "base/subscribe_email.html")
        response = self.client.get(reverse("Unsubscribed"))
        self.assertTemplateUsed(response, "base/unsubscibe.html")
        response = self.client.get(reverse("Newsletter"))
        self.assertTemplateUsed(response, "base/subscribe_form.html")

    def test_newsletter(self):
        self.login_admin()
        response = self.client.post(
            reverse("TestingEmail"),
            {
                "name": "test",
            },
        )
        self.assertRedirects(response, reverse("Newsletter"))
        response = self.client.post(
            reverse("Newsletter"),
            {
                "name": "test",
            },
        )
        self.assertRedirects(response, reverse("Newsletter"))
        response = self.client.get(reverse("TestingEmail"))
        self.assertTemplateUsed(response, "base/subscribe_form.html")

        

    def test_activate_account(self):
        subscribe = Subscribe.objects.create(name="test", email="test@gmail.com")
        subscribe.save()

        token = uuid4()
        response = self.client.get(
            reverse("VerifySubscribe", kwargs={"pk": subscribe.pk, "token": token})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base/subscribed.html")
