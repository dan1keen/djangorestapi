from requests import Response
from rest_framework import generics
from .models import Task,Tag
from .serializers import TasksSerializer, TagsSerializer, DetailTagSerializer, DetailTaskSerializer, AddTaskSerializer
from django.shortcuts import get_object_or_404

class ListTaskView(generics.ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TasksSerializer

class ListTagView(generics.ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagsSerializer

class DetailTaskView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class DetailTagView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = DetailTagSerializer

class AddTaskView(generics.CreateAPIView):
    serializer_class = AddTaskSerializer
    def create_task(request):
        serializer = AddTaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class AddTagView(generics.CreateAPIView):
    serializer_class = TagsSerializer
    def create_task(request):
        serializer = TagsSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tag created"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)