from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import basic


class basicinfo(ModelForm):
    class Meta:
        model = basic
        fields  = "__all__"

from dataclasses import fields

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']

        fields = ['username', 'email', 'password1']
