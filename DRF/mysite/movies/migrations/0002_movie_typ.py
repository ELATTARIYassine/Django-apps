# Generated by Django 3.1.4 on 2021-03-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
