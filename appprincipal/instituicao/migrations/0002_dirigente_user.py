# Generated by Django 3.0.6 on 2020-12-01 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirigente',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.Usuario'),
            preserve_default=False,
        ),
    ]