from rest_framework import serializers
from .models import Project, Task, SubTask
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'name', 'description']


class TaskSerializer(serializers.ModelSerializer):
    # subtasks = SubTaskSerializer(many=True, read_only=True)
    # assigned_to = UserSerializer(read_only=False)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description',
                  'start_date', 'end_date', 'assigned_to']


class ProjectSerializer(serializers.ModelSerializer):
    # tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "duration", "image"]
