# Generated by Django 3.1.4 on 2021-03-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://lh3.googleusercontent.com/proxy/GDrIX9vQID1NRs-pjKKk4vP3bMUegCU9QCEHPRGC6nvGaTNWJpBHYypmxjW0Ldv8tBlbyjnXG_ehn6wBwCGApLBMaiR9YEQrJ8m_lNSz4uxL0LyURtfA_KlpDGpekp5glutp6LNimBU-9yxAIWVlYeQ', max_length=500),
        ),
    ]
