# Generated by Django 4.2.13 on 2024-06-07 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('simbolo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.unidadmedida')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('numero_serie', models.CharField(max_length=200)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.marca')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenEgreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=250)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('destino', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.tipoequipo')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentesTipoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.tipoequipo')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentesEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.equipo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AppInventario.producto')),
            ],
        ),
    ]
