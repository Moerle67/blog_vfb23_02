# Generated by Django 5.0.1 on 2024-02-03 09:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50, verbose_name='Überschrift')),
                ('contents', models.TextField(verbose_name='Inhalt')),
                ('written', models.DateTimeField(auto_now_add=True, verbose_name='Geschrieben')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Geändert')),
                ('rating', models.IntegerField(default=5, verbose_name='Wertung (1-10)')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Tagebuch',
                'verbose_name_plural': 'Tagebücher',
            },
        ),
    ]
