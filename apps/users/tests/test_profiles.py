from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from apps.users.forms import UserUpdateForm,ProfileUpdateForm
from apps.users.models import Committee

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="TestUser")
        self.user.set_password("123456789")
        self.user.save()
        self.client.login(username="TestUser",password="123456789")


    def test_url(self):
        url = reverse("Profile",kwargs={"username":self.user.username})
        request = self.client.get(url)
        self.assertEqual(request.status_code,200)
    
    def test_profile_update(self):
        url = reverse("Update_Profile")
        request = self.client.get(url)
        self.assertEqual(request.status_code,200)
    
    def test_update_form(self):
        user_data = {
            "username": "TestUser1",
            'first_name':"Test",
            "last_name":"User",
            'email':"test@gmail.com"
        }
        form_u = UserUpdateForm(data=user_data)
        committee = Committee.objects.create(name="PR")
        committee.save()
        profile_data = {
            "bio": "asd",
            'image':"",
            "position":"Member",
            'committee': committee,
            "achievement":"Mew",
            "awards" : "Mwah",
            "experience" : "Mwah mwah"
        }
        form_p = ProfileUpdateForm(data=profile_data)

        self.assertTrue(form_u.is_valid())
        self.assertTrue(form_p.is_valid())

        form_u = UserUpdateForm(data={})
        form_p = ProfileUpdateForm(data={})
        self.assertFalse(form_u.is_valid())
        self.assertTrue(form_u.cleaned_data)
        self.assertFalse(form_p.is_valid())
        self.assertTrue(form_p.cleaned_data)

        


