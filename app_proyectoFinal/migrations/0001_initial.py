# Generated by Django 4.0.1 on 2022-01-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_inicio', models.DateField()),
                ('intensidad', models.CharField(max_length=10)),
                ('ejercicio_1', models.IntegerField()),
                ('ejercicio_2', models.IntegerField()),
                ('ejercicio_3', models.IntegerField()),
                ('ejercicio_4', models.IntegerField()),
                ('ejercicio_5', models.IntegerField()),
                ('ejercicio_6', models.IntegerField()),
                ('ejercicio_7', models.IntegerField()),
                ('duracionPorEjercicio', models.IntegerField()),
                ('descansoEntreEjercicio', models.IntegerField()),
                ('rondas', models.IntegerField()),
    
            ],
        ),
    ]
