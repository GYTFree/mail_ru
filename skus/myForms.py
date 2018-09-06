from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


class DemoForms(forms.Form):
    username = forms.CharField(min_length=6, error_messages={'invalid': '至少6个字符'})
    password = forms.CharField(widget=widgets.PasswordInput())
    re_password = forms.PasswordInput()
    email = forms.EmailField()