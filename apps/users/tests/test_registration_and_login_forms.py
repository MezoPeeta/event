from django.test import TestCase
from django.urls import reverse
from apps.users.models import RegistrationCode
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from apps.users.forms import UserRegisterForm


class TestRegistration(TestCase):
    def setUp(self):
        self.register_url = reverse("Register")
        self.registration_code = str(RegistrationCode.objects.all().last())
        self.user = {
            "username": "Mohammed234",
            "first_name": "Mohammed",
            "last_name": "Mohammed",
            "email": "email@gmail.com",
            "registration_code": self.registration_code,
            # "registration_code":"5952278197790206",
            "password1": "xysQ1234",
            "password2": "xysQ1234",
        }
        self.form = UserRegisterForm(data=self.user)

    def test_registration_form(self):
        self.assertTrue(self.form.is_valid())

    def test_username_field_empty(self):
        self.user.pop("username")
        self.assertFalse(self.form.is_valid())

    def test_first_name_field_empty(self):
        self.user.pop("first_name")
        self.assertTrue(self.form.is_valid())

    def test_last_name_field_empty(self):
        self.user.pop("last_name")
        self.assertTrue(self.form.is_valid())

    def test_code_field_empty(self):
        self.user.pop("registration_code")
        self.assertFalse(self.form.is_valid())

    def test_password1_field_empty(self):
        self.user.pop("password1")
        self.assertFalse(self.form.is_valid())

    def test_password2_field_empty(self):
        self.user.pop("password2")
        self.assertFalse(self.form.is_valid())

    def test_passowrd1_not_equal_passowrd2(self):
        self.user["password2"] = "Wrong password"
        self.assertFalse(self.form.is_valid())

    def test_password_less_than_8_characters(self):
        self.user["password1"] = "abc"
        self.assertFalse(self.form.is_valid())

    def test_password_entirely_numeric(self):
        self.user["password1"] = "12345678"
        self.assertFalse(self.form.is_valid())


class TestLogin(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="mahmoud", email="email@gmail.com", password="password"
        )
        self.user = {"username": "mahmoud", "password": "password"}
        self.form = AuthenticationForm(data=self.user)

    def test_login(self):
        self.assertTrue(self.form.is_valid())

    def test_empty_password_field(self):
        self.user.pop("password")
        self.assertFalse(self.form.is_valid())

    def test_empty_username_field(self):
        self.user.pop("username")
        self.assertFalse(self.form.is_valid())

    def test_wrong_password(self):
        self.user["password"] = ""
        self.assertFalse(self.form.is_valid())

    def test_wrong_username(self):
        self.user["username"] = "!"
        self.assertFalse(self.form.is_valid())
