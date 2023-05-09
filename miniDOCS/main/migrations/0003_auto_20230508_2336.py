# Generated by Django 3.2.13 on 2023-05-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tag_function'),
    ]

    operations = [
        migrations.AlterField(
            model_name='func',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='function',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.func'),
        ),
    ]