# Generated by Django 3.2.13 on 2023-05-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230509_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('size', models.CharField(max_length=2)),
                ('range', models.CharField(max_length=250)),
            ],
        ),
    ]