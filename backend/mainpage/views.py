from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MainPageUserSerializer, MainPageCommitSerializer
from .models import User, Comment

# Create your views here.

class MainPageUserViews(viewsets.ModelViewSet):
    serializer_class = MainPageUserSerializer
    queryset = User.objects.all()


class MainPageCommentViews(viewsets.ModelViewSet):
    serializer_class = MainPageCommitSerializer
    queryset = Comment.objects.all()



   