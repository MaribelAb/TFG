# Generated by Django 4.2.11 on 2024-05-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centaurApp', '0006_remove_dropdownfield_opciones_dropdownfield_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textfield',
            name='campo_ptr',
        ),
        migrations.RemoveField(
            model_name='opcion',
            name='dropdown_field',
        ),
        migrations.AddField(
            model_name='campo',
            name='opciones',
            field=models.ManyToManyField(blank=True, to='centaurApp.opcion'),
        ),
        migrations.DeleteModel(
            name='DropdownField',
        ),
        migrations.DeleteModel(
            name='TextField',
        ),
    ]
