# Generated by Django 3.0.6 on 2020-12-10 11:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0007_auto_20201210_0238'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DirigenteVal',
            new_name='DiretorPar',
        ),
        migrations.RenameModel(
            old_name='DiretorVal',
            new_name='DirigentePar',
        ),
    ]