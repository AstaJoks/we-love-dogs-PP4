from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import DateInput


class UpdateUserForm(forms.ModelForm):
    """Form class to update userprofile"""
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput
                               (attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', ]


class UpdateProfileForm(forms.ModelForm):
    """Form class to update profile"""
    bio = forms.CharField(required=False, widget=forms.Textarea
                          (attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'image',]
        labels = {
            'birth_date': ('Date of Birth'),
        }
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }
