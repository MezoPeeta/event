from django.test import TestCase
from utils.selenium_test import TestUtils
from apps.dashboard.models import Report
from django.urls import reverse
from apps.users.models import Committee

class TestReport(TestCase, TestUtils):
    def setUp(self):
        self.login_admin()
        committee = Committee.objects.create(name="Logistics")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()
        self.report = Report.objects.create(name="report", remarks="remark", author=self.user)

        
        

    def test_str_function(self):
        self.assertEqual(self.report.name, str(self.report))

    def test_get_absolute_url(self):
        absolute_url = reverse('Reports_Detail', kwargs={'pk':self.report.pk})
        self.assertEqual(absolute_url, self.report.get_absolute_url())
