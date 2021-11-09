from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TypeDonaiteSerializer
from .models import TypeDonaite



class TypeDonaiteViews(viewsets.ModelViewSet):
    serializer_class = TypeDonaiteSerializer
    queryset = TypeDonaite.objects.all()

