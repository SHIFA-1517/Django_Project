# Generated by Django 5.0 on 2025-01-25 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
