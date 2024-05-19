# Generated by Django 4.2.11 on 2024-05-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centaurApp', '0011_remove_campo_opciones_remove_formulario_campos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='formulario',
        ),
        migrations.RemoveField(
            model_name='opcion',
            name='campo',
        ),
        migrations.AddField(
            model_name='campo',
            name='opciones',
            field=models.ManyToManyField(blank=True, to='centaurApp.opcion'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='campos',
            field=models.ManyToManyField(blank=True, to='centaurApp.campo'),
        ),
    ]