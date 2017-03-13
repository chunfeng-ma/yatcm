# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0003_auto_20161102_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('phonetic_name', models.CharField(blank=True, max_length=1024)),
                ('describe', models.TextField(blank=True)),
                ('prescription_text', models.TextField(blank=True)),
                ('herbs', models.ManyToManyField(to='compounds.Herb')),
            ],
        ),
        migrations.AddField(
            model_name='compound',
            name='cid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.CID'),
        ),
    ]