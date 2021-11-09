from rest_framework import serializers
from .models import SucceesStories, OtherSuccessStories

class SucceesStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucceesStories
        fields = ('name', 'lastName', 'image', 'description')

class OtherSuccessStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSuccessStories
        fields = ('pib', 'numberTelephon', 'email', 'description')

