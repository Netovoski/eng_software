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

    nome_curso = models.CharField(max_length=50, null=False, blank=False)
    grau_curso = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    cod_emec = models.TextField(max_length=10, null=False, blank=False)    
        
    data_autorizacao = models.DateTimeField(auto_now_add= False, null=True)
    data_reconhecimento = models.DateTimeField(auto_now_add= False, null=True)
    data_renovacao = models.DateTimeField(auto_now_add= False, null=True)

    observacao = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.nome_curso
