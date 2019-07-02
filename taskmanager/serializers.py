from rest_framework import fields
from rest_framework import serializers
from .models import Tag, Task

class TasksSerializer(serializers.ModelSerializer):
    date_of_creation = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Task
        fields = ("id","task_name", "description","tags", "date_of_creation")

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag_name", "date_of_creation")

class DetailTaskSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Task
        fields = ("id","task_name", "description", "tags", "date_of_creation")


class DetailTagSerializer(serializers.ModelSerializer):
    task_list = DetailTaskSerializer(many=True)
    class Meta:
        model = Tag
        fields = ("tag_name", "date_of_creation", "task_list")


class AddTaskSerializer(serializers.ModelSerializer):
    date_of_creation = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=False)
    class Meta:
        model = Task
        fields = ("id","task_name", "description", "tags", "date_of_creation")