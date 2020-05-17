# Generated by Django 3.0.6 on 2020-05-17 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('crm', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('especialidade', models.CharField(blank=True, max_length=100)),
                ('chave_publica', models.CharField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'medico',
            },
        ),
    ]
