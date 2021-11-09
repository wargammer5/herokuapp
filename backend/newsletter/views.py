from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsletterSerializer
from .models import NewLetter

# Create your views here.

class NewsletterViews(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = NewLetter.objects.all()
