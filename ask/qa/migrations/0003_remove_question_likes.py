# Generated by Django 2.0 on 2020-04-06 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20200405_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
    ]