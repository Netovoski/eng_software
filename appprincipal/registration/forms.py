from appprincipal.registration.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']

class UserDeleteForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']
#class ProfileUpdateForm(forms.Model):