from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoListSerializer, FerramentaSerializer
from .models import TodoList, Ferramenta


class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class FerramentaViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer