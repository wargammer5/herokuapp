from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HebronOneHundredViews



router = routers.SimpleRouter()
router.register(r'hebronOneHundred', HebronOneHundredViews, 'HebronOneHundred')



urlpatterns = [
    path('', include(router.urls)),
]