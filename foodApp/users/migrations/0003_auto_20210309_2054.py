# Generated by Django 3.1.4 on 2021-03-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210309_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='profile_pictures'),
        ),
    ]
