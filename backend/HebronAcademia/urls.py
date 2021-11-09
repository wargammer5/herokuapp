"""HebronAcademia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from mainpage.views import MainPageUserViews , MainPageCommentViews
router = routers.SimpleRouter()
router.register(r'main-page-user', MainPageUserViews, 'main-page-user')
router.register(r'main-page-comment', MainPageCommentViews, 'main-page-comment')

from newsletter.views import NewsletterViews
router.register(r'newsletter', NewsletterViews, 'newslatter')

from stadies.views import SucceesStoriesViews,OtherSuccessStoriesViews
router.register(r'succees-story', SucceesStoriesViews, 'succees-story')
router.register(r'other-succees', OtherSuccessStoriesViews, 'other-success')

from type_of_donaite.views import TypeDonaiteViews
router.register(r'type-donaite', TypeDonaiteViews, 'type-donaite')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hebron100.urls')),
    path('', include(router.urls)),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)