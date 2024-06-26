# Generated by Django 4.2.11 on 2024-04-24 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('solicitante', models.CharField(max_length=100, verbose_name='Solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('fecha_fin', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('prioridad', models.CharField(blank=True, choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], max_length=6)),
                ('estado', models.CharField(blank=True, choices=[('abierto', 'Abierto'), ('en_curso', 'En curso'), ('cerrado', 'Cerrado')], max_length=10)),
                ('fecha_ini', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('nota', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nota')),
                ('carpeta', models.CharField(blank=True, max_length=100, null=True, verbose_name='Carpeta')),
                ('categoria', models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria')),
                ('conversacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='centaurApp.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='centaurApp.usuario')),
                ('lista_tickets', models.ManyToManyField(blank=True, to='centaurApp.ticket')),
                ('tareas', models.ManyToManyField(blank=True, to='centaurApp.tarea')),
            ],
            options={
                'abstract': False,
            },
            bases=('centaurApp.usuario',),
        ),
    ]
