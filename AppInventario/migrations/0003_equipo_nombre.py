# Generated by Django 4.2.13 on 2024-06-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario', '0002_alter_producto_numero_serie'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]