from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Task, SubTask
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, SubTaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
# Create your views here.


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TaskList(APIView):
    def get_object(self, project_id):
        project = get_object_or_404(Project, pk=project_id)
        task = project.tasks.all()
        return task

    def get(self, request, project_id):
        task = self.get_object(project_id)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)


class SubTaskList(APIView):
    def get_object(self, project_id, task_id):
        project = get_object_or_404(Project, pk=project_id)
        task = get_object_or_404(project.tasks, pk=task_id)
        subtask = task.subtasks.all()
        return subtask

    def get(self, request, project_id, task_id):
        subtask = self.get_object(project_id, task_id)
        serializer = SubTaskSerializer(subtask, many=True)
        return Response(serializer.data)


class ProjectCreate(APIView):
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskCreate(APIView):
    def get_object(self, project_id):
        project = get_object_or_404(Project, pk=project_id)
        task = Task(project=project)
        return task

    def post(self, request, project_id):
        task = self.get_object(project_id)
        print(request.data)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskCreate(APIView):
    def get_object(self, project_id, task_id):
        project = get_object_or_404(Project, pk=project_id)
        task = get_object_or_404(project.tasks, pk=task_id)
        subtask = SubTask(task=task)
        return subtask

    def post(self, request, project_id, task_id):
        subtask = self.get_object(project_id, task_id)
        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    def get_object(self, project_id):
        project = get_object_or_404(Project, pk=project_id)
        return project

    def get(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

    def put(self, request, project_id):
        project = self.get_object(project_id)
        serializer = ProjectSerializer(instance=project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id):
        project = self.get_object(project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetail(APIView):
    def get_object(self, project_id, task_id):
        project = get_object_or_404(Project, pk=project_id)
        task = get_object_or_404(project.tasks, pk=task_id)
        return task

    def get(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    def put(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, task_id):
        task = self.get_object(project_id, task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubTaskDetail(APIView):
    def get_object(self, project_id, task_id, subtask_id):
        project = get_object_or_404(Project, pk=project_id)
        task = get_object_or_404(project.tasks, pk=task_id)
        subtask = get_object_or_404(task.subtasks, pk=subtask_id)
        return subtask

    def get(self, request, project_id, task_id, subtask_id):
        subtask = self.get_object(project_id, task_id, subtask_id)
        serializer = SubTaskSerializer(subtask, many=False)
        return Response(serializer.data)

    def put(self, request, project_id, task_id, subtask_id):
        subtask = self.get_object(project_id, task_id, subtask_id)
        serializer = SubTaskSerializer(instance=subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, task_id, subtask_id):
        subtask = self.get_object(project_id, task_id, subtask_id)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
