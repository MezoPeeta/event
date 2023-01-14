from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core import validators

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[validators.validate_email])
    registration_code = forms.CharField(max_length=16)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','registration_code','password1', 'password2', ]
    
    def isExists(self):
        if User.objects.filter(email = self.email):
            return True
        else:
            return False


# USER UPDATE FORM!!
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

#PROFILE UPDATE FORM
class ProfileUpdateForm(forms.ModelForm):
     


    class Meta:
        model = Profile
        fields = ['bio', 'image', 'position' ,'committee', 'achievement','awards', 'experience']
