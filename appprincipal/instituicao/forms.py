from appprincipal.instituicao.models import *
from django import forms
from django.forms import ModelForm

class RegistrarUniversidadeCentralForm(forms.ModelForm):

    class Meta:
        model = Instituicao
        fields='__all__'

class RegistrarDirigenteForm(forms.ModelForm):

    class Meta:
        model = Dirigente
        fields='__all__'



class RegistrarUniversidadeForm(forms.ModelForm):

    class Meta:
        model = Instituicao
        fields='__all__'