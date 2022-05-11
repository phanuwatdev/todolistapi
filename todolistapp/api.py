from rest_framework import routers, viewsets, serializers
from .models import Todolist
from .serializer import TodolistSerializer

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.filter(published=True)
    serializer_class = TodolistSerializer

router = routers.SimpleRouter()
router.register(r'todolist', TodolistViewSet)