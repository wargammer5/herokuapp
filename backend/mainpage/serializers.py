from rest_framework import serializers
from .models import User, Comment

class MainPageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lastname', 'email', 'password', 'verificPassword')

        
class MainPageCommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'description')

