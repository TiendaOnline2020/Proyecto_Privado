# Generated by Django 3.0.3 on 2020-02-25 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=255)),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('region_provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Region')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('provincia_id', models.IntegerField(blank=True, null=True)),
                ('provincia_distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Provincia')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
            },
        ),
    ]
