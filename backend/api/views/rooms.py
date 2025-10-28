from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Room
from ..serializers import RoomSerializer
from ..permissions import IsAdminOrReadOnly

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]