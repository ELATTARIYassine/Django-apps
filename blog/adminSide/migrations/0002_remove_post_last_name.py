# Generated by Django 3.1.4 on 2021-03-24 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
    ]
