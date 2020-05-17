# Generated by Django 3.0.6 on 2020-05-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, verbose_name='Data de Nascimento')),
                ('telefone', models.CharField(max_length=30)),
                ('cpf', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
    ]