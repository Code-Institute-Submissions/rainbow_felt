from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import UserExtras


# Registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Form for extra details for user
class ExtrasForm(forms.ModelForm):
    class Meta:
        model = UserExtras
        exclude = ['user']
        fields = ['house', 'street', 'city', 'postcode']


# Login form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
