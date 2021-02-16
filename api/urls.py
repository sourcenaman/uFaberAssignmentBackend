from django.urls import path
from . import views

urlpatterns = [
    path("users", views.UserList.as_view(), name="UserList"),
    path("project", views.ProjectList.as_view(), name="ProjectList"),
    path("project/<int:project_id>",
         views.ProjectDetail.as_view(), name="ProjectDetail"),
    path("project/<int:project_id>/task",
         views.TaskList.as_view(), name="TaskList"),
    path("project/<int:project_id>/task/<int:task_id>",
         views.TaskDetail.as_view(), name="TaskDetail"),
    path("project/<int:project_id>/task/<int:task_id>/subtask",
         views.SubTaskList.as_view(), name="SubTaskList"),
    path("project/<int:project_id>/task/<int:task_id>/subtask/<int:subtask_id>",
         views.SubTaskDetail.as_view(), name="SubTaskDetail"),
    path("project/create", views.ProjectCreate.as_view(), name="ProjectCreate"),
    path("project/<int:project_id>/task/create",
         views.TaskCreate.as_view(), name="TaskCreate"),
    path("project/<int:project_id>/task/<int:task_id>/subtask/create",
         views.SubTaskCreate.as_view(), name="SubTaskCreate"),
]
