#encoding=utf-8
from django import forms
from captcha.fields import CaptchaField


class LoginForms(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField()

