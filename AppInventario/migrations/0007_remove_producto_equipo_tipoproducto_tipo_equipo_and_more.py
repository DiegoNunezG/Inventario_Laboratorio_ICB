# Generated by Django 4.2.13 on 2024-06-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario', '0006_producto_equipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='equipo',
        ),
        migrations.AddField(
            model_name='tipoproducto',
            name='tipo_equipo',
            field=models.ManyToManyField(to='AppInventario.tipoequipo'),
        ),
        migrations.DeleteModel(
            name='ComponentesTipoEquipo',
        ),
    ]
