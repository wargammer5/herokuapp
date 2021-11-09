from rest_framework import serializers
from .models import NewLetter

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLetter
        fields = ('photo', 'title', 'description', 'choiseTypeNews')

