from django.urls import path, include
from . import views
from .viewsets import UserAPIViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserAPIViewSet, 'user')

urlpatterns = [
    path('', include(router.urls), name='user'),
]
