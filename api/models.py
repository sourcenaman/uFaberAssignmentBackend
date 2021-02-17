from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='avatars', default='default.jpg')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True, null=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubTask(models.Model):
    task = models.ForeignKey(
        Task, related_name="subtasks", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
