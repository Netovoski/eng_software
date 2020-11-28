from django.db import models

# Create your models here.


class Curso(models.Model):
	nome_curso = models.CharField( max_length=50, null=False, blank=False)
	precoprod = models.DecimalField( max_digits=8, decimal_places=2, null=False, blank=False )
    
	id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)


    cod_emec = models.IntegerField( max_digits=8, null=False, blank=False)

    grau_curso = models.IntegerField( max_digits=8, null=False, blank=False)

    data_autorização = models.DateTimeField(auto_now_add= Falso, null=True)
    data_publicacao = models.DateTimeField(auto_now_add= Falso, null=True)
    data_renovacao = models.DateTimeField(auto_now_add= Falso, null=True)

    descricao = models.CharField(max_length=200, null=True)


	def __str__(self):
		return f'{self.nome_curso}'
