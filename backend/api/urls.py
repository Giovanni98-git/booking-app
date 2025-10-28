from django.urls import path
from .views import (RoomListCreateView, RoomDetailView, api_root,
                    OccupiedDateListCreateView, OccupiedDateDetailView
                    , UserListView, UserDetailView, Register, Login)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', api_root, name='api-root'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('occupied-dates/', OccupiedDateListCreateView.as_view(), name='occupieddate-list'),
    path('occupied-dates/<int:pk>/', OccupiedDateDetailView.as_view(), name='occupieddate-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)