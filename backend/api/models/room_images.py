from django.db import models

class RoomImage(models.Model):
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey('Room', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.room.name} - {self.caption or 'No Caption'}"