from django.db import models
from .rooms import Room
from django.conf import settings

class OccupiedDate(models.Model):
    room = models.ForeignKey(Room, related_name='occupiedDates', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='booked_dates', on_delete=models.CASCADE)  
    date = models.DateField()
    
    def __str__(self):
        return f"{self.room.name} occupied on {self.date} by {self.user.username}"
    