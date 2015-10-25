# forms.py - opinify
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email', 'first_name', 'last_name')

	password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())