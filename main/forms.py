from django import forms
from django.contrib.auth.models import User
from main.models import UserIWM, IWM


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserFormLast(forms.ModelForm):
    class Meta:
        model = UserIWM
        fields = ('phone', 'photo', 'is_parent')


class IWMForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = IWM
        fields = ('username', 'password', 'first_name', 'last_name', 'phone', 'photo', 'is_parent')
