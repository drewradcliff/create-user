from django import forms
from django.contrib.auth.forms import UserCreationForm
from custom_users.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    # username = forms.CharField(max_length=240)
    # name = forms.CharField(max_length=80)
    # age = forms.IntegerField()
    # homepage = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ["username", "name", "age", "homepage"]
