from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe Room'),
        ('standard', 'Standard Room')
    ]
    CURRENCY_TYPES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound')
    ]
    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, choices=ROOM_TYPES)
    pricePerNight = models.IntegerField(default=150)
    currency = models.CharField(default='USD', max_length=10, choices=CURRENCY_TYPES )
    maxOccupancy = models.IntegerField(default=1)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} ({self.type})"