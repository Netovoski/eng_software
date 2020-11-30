from django.db import models

# Create your models here.

class Instituicao(models.Model):
	nome_instituicao = models.CharField( max_length=50, null=False, blank=False)
	#precoprod = models.DecimalField( max_digits=8, decimal_places=2, null=False, blank=False )
    
	usuario = models.ForeignKey(Instituicao, on_delete=models.CASCADE)


    credenciamento = models.IntegerField( max_digits=6, null=False, blank=False)

    grau_curso = models.IntegerField( max_digits=8, null=False, blank=False)

    data_autorização = models.DateTimeField(auto_now_add= Falso, null=True)
    data_publicacao = models.DateTimeField(auto_now_add= Falso, null=True)
    data_renovacao = models.DateTimeField(auto_now_add= Falso, null=True)

    descricao = models.CharField(max_length=200, null=True)


	def __str__(self):
		return f'{self.nome_curso}'

class Dirigente(models.Model):

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField( max_length=255,null=False, blank=False)
    cpf = models.IntegerField( max_length = 255, null = False, blank= False)
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