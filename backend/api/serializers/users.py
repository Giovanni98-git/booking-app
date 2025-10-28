from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'full_name', 'password']
        
        def validate_password(self, value):
            return make_password(value)