# Generated by Django 4.2.11 on 2024-06-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centaurApp', '0022_ticket_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='encargado',
            field=models.CharField(default='Sin asignar', max_length=100, verbose_name='Encargado'),
        ),
    ]
