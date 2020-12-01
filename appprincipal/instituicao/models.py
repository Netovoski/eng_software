from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from appprincipal.registration.models import *


class Instituicao(models.Model):
	
    nome_instituicao = models.CharField(max_length=50,null=False,blank=False)
    credenciamento = models.IntegerField()
    grau_curso = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    data_autorização = models.DateTimeField(auto_now_add= False, null=True)
    data_publicacao = models.DateTimeField(auto_now_add= False, null=True)
    data_renovacao = models.DateTimeField(auto_now_add= False, null=True)

    descricao = models.CharField(max_length=200, null=True)
    #usuario = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_instituicao


class Dirigente(models.Model):

    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField( max_length=255,null=False, blank=False)
    cpf = models.IntegerField()
    e_mail = models.CharField( max_length=255,null=False, blank=False)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    
    #cliente = models.ForeignKey(Cliente,verbose_name="Cliente")
    rua = models.CharField("Rua",max_length=100)
    numero = models.IntegerField("Numero",max_length=100)
    complemento = models.CharField("Complemento",max_length=100)
    bairro = models.CharField("Bairro",max_length=100)
    cidade = models.CharField("Cidade",max_length=100)
    estado = models.CharField("Estado",max_length=2)
    cep = models.CharField("Cep",max_length=8)
    
    def __unicode__(self):
        return "%s, %s - %s" % (self.rua,self.numero,self.cep)