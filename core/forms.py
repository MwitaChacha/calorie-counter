from django import forms
from .models import *
from django.forms import ModelForm, DateInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        widgets = {
              'schedule_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
              
            }   
        fields = ['food','accompaniment','meal','schedule_time']