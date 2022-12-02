from django.test import TestCase, Client
from django.shortcuts import reverse 

class TestingDashboard(TestCase):
    def test_dashboard(self):
        url = reverse('Dashboard')
        request = self.client.get(url)
        self.assertEquals(request.status_code,302) #Testing login required

        self.assertTemplateUsed(request.templates,'dashboard/PR/dashboard.html')