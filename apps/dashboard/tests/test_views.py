from django.test import TestCase, LiveServerTestCase
from django.shortcuts import reverse
from utils.selenium_test import TestUtils
from selenium.webdriver.common.by import By
from apps.products.models import Products
from apps.base.models import Contact
from apps.dashboard.views import ContactForm
from apps.users.models import Committee


class TestViews(TestCase, TestUtils):
    def setUp(self):
        self.login_admin()

    def test_us(self):
        committee = Committee.objects.create(name="IT")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()
        url = reverse("Dashboard")
        request = self.client.get(url)
        self.assertEqual(request.status_code, 302)

    def test_reverse(self):
        committee = Committee.objects.create(name="HR")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()

        Contact.objects.create(
            name="Contact1",
            email="marwanmoatassem@gmail.com",
            subject="7amam",
            message="nam",
        )
        url = reverse("Inbox_Detail", kwargs={"pk": 1})

        request = self.client.post(url, data={"reply": "Hello WOrld"})

        self.assertEqual(request.status_code, 302)

    def test_get_context_data(self, **kwargs):
        committee = Committee.objects.create(name="HR")
        committee.save()

        self.user.profile.committee = committee
        self.user.profile.save()
        Contact.objects.create(
            name="Contact1",
            email="marwanmoatassem@gmail.com",
            subject="7amam",
            message="nam",
        )
        url = reverse("Inbox_Detail", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.context["form"], ContactForm)

    def test_form_invalid(self):
        committee = Committee.objects.create(name="HR")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()

        reverse("Inbox_Detail", kwargs={"pk": 1})
        form = ContactForm(
            data={
                "name": "marwan",
                "email": "marawnmoatassem@gm@@ail.com",
                "subject": "marwan",
                "message": "marwan",
                "reply": "MSG",
            }
        )
        self.assertTrue(form.is_valid())
        form = ContactForm(
            data={
                "name": "marwan",
                "email": "marawnmoatassem@gm@@ail.com",
                "subject": "marwan",
                "message": "marwan",
            }
        )
        self.assertFalse(form.is_valid())


    def test_InboxDelete(self):
        committee = Committee.objects.create(name="HR")
        self.user.profile.committee = committee
        self.user.profile.save()
        Contact.objects.create(
            name="Test",
            email="test@gmail.com",
            subject="Test_Subject",
            message="Test_Message",
            reply="Test_Reply",
        )
        url = reverse("Inbox_Delete", kwargs={"pk": 1})
        request = self.client.get(url)
        print("url:", request.status_code)
        self.assertTemplateUsed("dashboard/HR/inbox.html")

