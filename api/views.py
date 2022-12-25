from django.shortcuts import render
from .models import Tag, Task
from rest_framework import viewsets
from .serializers import TagSerializer, TaskSerializer
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer