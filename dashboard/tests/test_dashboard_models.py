from django.test import TestCase
from utils.selenium_test import TestUtils
from dashboard.models import Report, Design
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Committee

class TestReport(TestCase, TestUtils):
    def setUp(self):
        self.login_admin()
        committee = Committee.objects.create(name="Logistics")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()
        self.report = Report.objects.create(name="report", remarks="remark", author=self.user)

        
        

    def test_str_function(self):
        self.assertEquals(self.report.name, str(self.report), self.report.__str__())

    def test_get_absolute_url(self):
        # response = self.client.get(reverse('Reports_Detail', kwargs={'pk':self.report.pk}))
        # self.assertEquals(response.status_code, 200)
        absolute_url = reverse('Reports_Detail', kwargs={'pk':self.report.pk})
        self.assertEquals(absolute_url, self.report.get_absolute_url())
class TestDesign(TestCase):
    def setUp(self):
        self.design = Design.objects.create()
    def test_str_function(self):
        self.assertEquals(self.design.color, self.design.__str__(),str(self.design))
    