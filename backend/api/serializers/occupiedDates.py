from rest_framework import serializers
from ..models import OccupiedDate, Room
class OccupiedDateSeriailizer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name='room-detail', queryset= Room.objects.all())
    class Meta:
        model = OccupiedDate
        fields = ['url','id', 'room', 'date']