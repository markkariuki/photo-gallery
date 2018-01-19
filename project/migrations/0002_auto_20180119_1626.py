# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='photos/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_descripton', models.TextField()),
                ('image_category', models.ManyToManyField(to='project.categories')),
                ('location_taken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.location')),
            ],
        ),
        migrations.DeleteModel(
            name='tags',
        ),
    ]
