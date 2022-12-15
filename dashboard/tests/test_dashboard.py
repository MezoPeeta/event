from django.contrib.auth.models import User
from django.test import TestCase 
from django.shortcuts import reverse 
from users.models import Profile

class TestingDashboard(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Test")
        self.user.set_password("123456789")
        self.user.save()
        self.client.login(username='Test', password='123456789')
        self.user.profile.committee = "PR"
        self.user.profile.save()
        
    def test_dashboard(self):
        url = reverse('Dashboard')
        request = self.client.get(url)     
        # testing dashboard page
        self.assertEquals(request.status_code, 200)

            
        
        
