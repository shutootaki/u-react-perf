from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('tags', TagViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]