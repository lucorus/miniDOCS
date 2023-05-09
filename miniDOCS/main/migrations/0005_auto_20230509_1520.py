# Generated by Django 3.2.13 on 2023-05-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230509_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='func',
            name='library',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='func',
            name='type_return',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='function',
        ),
        migrations.AddField(
            model_name='tag',
            name='function',
            field=models.ManyToManyField(blank=True, to='main.Func'),
        ),
    ]
