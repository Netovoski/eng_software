from appprincipal.instituicao.models import *
from appprincipal.registration.models import *
from django import forms
from django.forms import ModelForm

class RegistrarInst_ParForm(forms.ModelForm):

    class Meta:
        model = Inst_Par
        fields='__all__'

class RegistrarInst_ValForm(forms.ModelForm):

    class Meta:
        model = Inst_Val
        fields='__all__'

class RegistrarDirigenteParForm(forms.ModelForm):

    class Meta:
        model = DirigentePar
        fields='__all__'

class RegistrarDirigenteValForm(forms.ModelForm):

    class Meta:
        model = DirigenteVal
        fields='__all__'

class RegistrarDiretorParForm(forms.ModelForm):

    class Meta:
        model = DiretorPar
        fields='__all__'

class RegistrarSuperValForm(forms.ModelForm):

    class Meta:
        model = SuperVal
        fields='__all__'

class RegistrarUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields='__all__'

# class RegistrarInst_ParForm(forms.ModelForm):

#     class Meta:
#         model = Inst_Parc
#         fields='__all__'




# class RegistrarDirigenteForm(forms.ModelForm):

#     class Meta:
#         model = Dirigente
#         fields='__all__'



# class RegistrarUniversidadeForm(forms.ModelForm):

#     class Meta:
#         model = Instituicao
#         fields='__all__'