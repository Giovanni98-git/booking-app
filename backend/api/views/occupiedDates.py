from ..models import OccupiedDate
from ..serializers.occupiedDates import OccupiedDateSeriailizer
from rest_framework import generics, permissions
from ..permissions import IsAdminOrReadOnly

class OccupiedDateListCreateView(generics.ListCreateAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSeriailizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser or not user.is_staff:
            return OccupiedDate.objects.filter(user=user)
        return super().get_queryset()


class OccupiedDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSeriailizer
    permission_classes = [IsAdminOrReadOnly]