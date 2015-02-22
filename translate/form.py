__author__ = 'andriy'
from django import forms
from django.contrib.auth.models import User
from translate.models import  NewSong


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserAddSongForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    name_ukr = forms.CharField(widget=forms.TextInput())
    text_ukr = forms.CharField(widget=forms.Textarea())
    text_org = forms.CharField(widget=forms.Textarea())
    band = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = NewSong
        fields = ("name", "name_ukr", "text_ukr", "text_org","band")