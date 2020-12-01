from django.db import models
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from appprincipal.registration.models import *
from appprincipal.instituicao.models import *


class Curso(models.Model):

    
    cod_emec = models.IntegerField(max_length=8, null=False, blank=False)

	#

    grau_curso = models.IntegerField(max_length=8, null=False, blank=False)
    data_autorização = models.DateTimeField(auto_now_add= False, null=True)
    data_publicacao = models.DateTimeField(auto_now_add= False, null=True)
    data_renovacao = models.DateTimeField(auto_now_add= False, null=True)
    descricao = models.CharField(max_length=200, null=True)
    nome_curso = models.CharField(max_length=50, null=False, blank=False)
    
	#precoprod = models.DecimalField( max_digits=8, decimal_places=2, null=False, blank=False )
    
	#id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso
