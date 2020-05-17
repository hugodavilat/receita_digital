# Generated by Django 3.0.6 on 2020-05-17 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('doctors', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(blank=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False)),
                ('signature', models.CharField(blank=True, max_length=256)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctors.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patients.Paciente')),
                ('posologias', models.ManyToManyField(to='main.Posologia')),
            ],
            options={
                'db_table': 'receita',
            },
        ),
    ]
