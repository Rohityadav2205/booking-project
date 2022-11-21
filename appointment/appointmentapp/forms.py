from django import forms
from django.forms import ModelForm
from .models import BookingModel


class BookingForm( ModelForm):
    class Meta:
        model=BookingModel
        fields="__all__"

# class VisitForm(forms.Form):
#     Mobile_No=forms.IntegerField()
#     Random_No=forms.IntegerField()