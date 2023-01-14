from django.test import TestCase 
from django.shortcuts import reverse 
from selenium_test import TestUtils

class TestingDashboard(TestCase,TestUtils):
    def setUp(self):
        self.login_admin()
        
    def test_dashboard(self):
        self.user.profile.committee = "PR"
        self.user.profile.save()
        url = reverse('Dashboard')
        request = self.client.get(url)     
        # testing dashboard page
        self.assertEquals(request.status_code, 200)

            
        
        
