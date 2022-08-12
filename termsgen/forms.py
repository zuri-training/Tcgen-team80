from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import basic


class basicinfo(ModelForm):
    class Meta:
        model = basic
        fields  = "__all__"

