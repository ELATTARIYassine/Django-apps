from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default="https://lh3.googleusercontent.com/proxy/GDrIX9vQID1NRs-pjKKk4vP3bMUegCU9QCEHPRGC6nvGaTNWJpBHYypmxjW0Ldv8tBlbyjnXG_ehn6wBwCGApLBMaiR9YEQrJ8m_lNSz4uxL0LyURtfA_KlpDGpekp5glutp6LNimBU-9yxAIWVlYeQ")

    def __str__(self):
        return self.name