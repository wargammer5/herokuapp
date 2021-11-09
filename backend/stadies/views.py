from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SucceesStoriesSerializer,OtherSuccessStoriesSerializer
from .models import SucceesStories, OtherSuccessStories

# Create your views here.

class SucceesStoriesViews(viewsets.ModelViewSet):
    serializer_class = SucceesStoriesSerializer
    queryset = SucceesStories.objects.all()


class OtherSuccessStoriesViews(viewsets.ModelViewSet):
    serializer_class = OtherSuccessStoriesSerializer
    queryset = OtherSuccessStories.objects.all()
