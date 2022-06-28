# Generated by Django 3.0 on 2022-06-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_visitante_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='cargo_visitante',
            field=models.CharField(choices=[('MOTORISTA', 'Motorista'), ('AJUDANTE', 'Ajudante'), ('DIRETORIA', 'Funcionario da Direção'), ('COMUM', 'Funcionario comum')], default='COMUM', max_length=20, verbose_name='Cargo visitante'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='numero_casa',
            field=models.CharField(max_length=2, verbose_name='Numero da casa a ser visitada'),
        ),
    ]