from ..models import User
from ..serializers.users import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser or not user.is_staff:
            return User.objects.filter(id=user.id)
        return super().get_queryset()
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        user = self.request.user
        obj =  super().get_object()
        
        if obj == user or user.is_superuser or user.is_staff:
            return obj
        else:
            raise permissions.PermissionDenied("You do not have permission to access this user's details.")
        
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        
        token, created = Token.objects.get_or_create(user=user)
        
        self.response_data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name": user.full_name,
            }, 
            "token": token.key
        }
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(self.response_data, status=status.HTTP_201_CREATED)

class Login(APIView):
    def post(sel, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise AuthenticationFailed("Invalid username or password")
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name": user.full_name,
            },
            "token": token.key
        })