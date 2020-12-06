from appprincipal.curso.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarTipoCursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields='__all__'