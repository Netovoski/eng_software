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


class Inst(models.Model):
    class Meta:
        abstract = True	

    nome_instituicao = models.CharField(max_length=50,null=False,blank=False)
    endereco = models.CharField("Endereço",max_length=100)
    cidade = models.CharField("Cidade",max_length=100)
    estado = models.CharField("Estado",max_length=2)
    credenciamento = models.IntegerField()
    mantenedora = models.CharField(max_length=50,null=False,blank=False)
    descricao = models.CharField(max_length=200, null=True)   
    #dirigente = models.ForeignKey(Dirigente,on_delete=models.CASCADE)#senha não mostra
    #funcionario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):#confirmação
        return self.nome_instituicao

class Inst_Par(Inst):
    
    dirigente = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
    #diretor = models.ForeignKey(User, on_delete = models.CASCADE ) #colocar tipo usuario

class Inst_Val(Inst):
    
    superitende = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
    #diretor = models.ForeignKey(User, on_delete = models.CASCADE ) #colocar tipo usuario




# class Inst_Parc(Inst):
#     diretor = models.CharField(max_length=50,null=False,blank=False)



# class Inst_Val(models):
#     #herda inst
#     #superintendente/ coordenador do Care
    
# class Inst_Parc(models):
#     #herda inst
#     #Diretor







