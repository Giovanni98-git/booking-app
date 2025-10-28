from rest_framework import serializers
from ..models import Room, RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name='room-detail', queryset = Room.objects.all())
    class Meta:
        model = RoomImage
        fields = ['id', 'room', 'image', 'caption']