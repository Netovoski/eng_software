from appprincipal.curso.models import *
from django import forms
from django.forms import ModelForm

class RegistrarTipoCursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields='__all__'