# Generated by Django 3.0.14 on 2022-01-23 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'segment',
                'verbose_name_plural': 'segmenti',
                'ordering': ('naziv',),
            },
        ),
        migrations.CreateModel(
            name='Trotinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('slika', models.ImageField(blank=True, upload_to='trotinet/%Y/%m/%d')),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('raspoloziv', models.BooleanField(default=True)),
                ('kreiran', models.DateTimeField(auto_now_add=True)),
                ('azuriran', models.DateTimeField(auto_now=True)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trotineti', to='ProdavnicaTrotineta.Segment')),
            ],
            options={
                'verbose_name_plural': 'trotineti',
                'ordering': ('naziv',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
