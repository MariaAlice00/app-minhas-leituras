# Generated by Django 3.2.3 on 2021-05-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('serie_unico', models.CharField(max_length=50)),
                ('nota', models.FloatField()),
                ('opiniao', models.CharField(max_length=300)),
            ],
        ),
    ]
