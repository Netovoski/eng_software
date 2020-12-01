# Generated by Django 3.0.6 on 2020-12-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dirigente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.IntegerField()),
                ('e_mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.IntegerField(max_length=100, verbose_name='Numero')),
                ('complemento', models.CharField(max_length=100, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=8, verbose_name='Cep')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=50)),
                ('credenciamento', models.IntegerField()),
                ('grau_curso', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('data_autorização', models.DateTimeField(null=True)),
                ('data_publicacao', models.DateTimeField(null=True)),
                ('data_renovacao', models.DateTimeField(null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
