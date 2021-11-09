from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MainPageViewsViews


router = routers.SimpleRouter()
router.register(r'mainPage', MainPageViewsViews, 'mainPage')


urlpatterns = [
    path('', include(router.urls)),
]