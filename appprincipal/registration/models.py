from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from appprincipal.diploma.models import *
from appprincipal.instituicao.models import *
# from appprincipal.curso.models import *

class Tipo_Usuario(models.Model):
	tipo_user = models.CharField(max_length=200, null=False)
	#Dirigente, diretor, funcionario, superintendente, coordenador CARE
		
	def __str__(self):
		return self.tipo_user

class Usuario(models.Model):
	#user = models.CharField(max_length=200, null=True ) #colocar tipo usuario
	instituicao = models.ForeignKey(Inst_Par,on_delete=models.CASCADE)
	tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	sobrenome = models.CharField(max_length=200, null=True)
	cpf = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	#email = models.CharField(max_length=200, null=True)
	
	#instituicao = models.OneToOneField(Inst,on_delete=models.CASCADE)
	def __str__(self):
		return self.nome




class DirigentePar(models.Model):#cadastra instituição parceira / Validadora
	user = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
	instituicao = models.ForeignKey(Inst_Par,on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	sobrenome = models.CharField(max_length=200, null=True)
	cpf = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.user

class DiretorPar(models.Model):#cadastra instituição parceira / Validadora
	user = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
	instituicao = models.ForeignKey(Inst_Par,on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	sobrenome = models.CharField(max_length=200, null=True)
	cpf = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.user


class DirigenteVal(models.Model):#cadastra instituição parceira / Validadora
	user = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
	instituicao = models.ForeignKey(Inst_Val,on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	sobrenome = models.CharField(max_length=200, null=True)
	cpf = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.user

class SuperVal(models.Model):#cadastra instituição parceira / Validadora
	user = models.OneToOneField(User, on_delete = models.CASCADE ) #colocar tipo usuario
	instituicao = models.ForeignKey(Inst_Val,on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	sobrenome = models.CharField(max_length=200, null=True)
	cpf = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	
	
	def __str__(self):
		return self.user