from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HebronOneHundredSerializer
from .models import FormDonaite

# Create your views here.

class HebronOneHundredViews(viewsets.ModelViewSet):
    serializer_class = HebronOneHundredSerializer
    queryset = FormDonaite.objects.all()