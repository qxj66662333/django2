# Generated by Django 2.1.5 on 2019-12-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20191230_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
