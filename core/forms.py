from django import forms
from .models import *
from django.forms import ModelForm, DateInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


