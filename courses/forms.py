from django.forms import ModelForm
from django import forms
from .models import courses
from .models import student




class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'