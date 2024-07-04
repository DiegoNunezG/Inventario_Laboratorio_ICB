# Generated by Django 4.2.13 on 2024-07-03 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario', '0023_proveedor_comuna_proveedor_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.region')),
            ],
            options={
                'unique_together': {('nombre', 'region')},
            },
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.comuna'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.region'),
        ),
    ]
