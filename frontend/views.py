from django.shortcuts import render, redirect
from django.views import View
import requests

# Create your views here.


class ProjectCreate(View):
    def post(self, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/create"
        payload = {
            "name": request.POST['name']
        }
        requests.post(api_url, data=payload)
        return redirect('ProjectList')


class ProjectUpdate(View):
    template = 'frontend/project_form.html'

    def get_object(self, project_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id):
        response = self.get_object(project_id, request)
        context = {
            'project': response
        }
        return render(request, self.template, context)

    def post(self, request, project_id):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}"
        payload = {
            "id": project_id,
            "name": request.POST['name'],
            "description": request.POST['description'],
            "duration": request.POST['duration'],
            # "image": request.FILES['image'],
        }
        try:
            image_payload = {"image": request.FILES['image']}

            requests.put(api_url, data=payload, files=image_payload)
        except:
            requests.put(api_url, data=payload)
        return redirect('ProjectDetail', project_id=project_id)


class ProjectList(View):
    template = 'frontend/project_list.html'

    def get(self, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + "api/project"
        response = requests.get(api_url).json()
        context = {
            'projects': response
        }
        return render(request, self.template, context)


class ProjectDetail(View):
    template = 'frontend/project.html'

    def get_object(self, project_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id):
        response = self.get_object(project_id, request)
        context = {
            'project': response
        }
        return render(request, self.template, context)


class TaskCreate(View):
    def post(self, request, project_id):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task/create"
        payload = {
            "name": request.POST['name']
        }
        requests.post(api_url, data=payload)
        return redirect('TaskList', project_id=project_id)


class TaskUpdate(View):
    template = 'frontend/task_form.html'

    def get_object(self, project_id, task_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task/{task_id}"
        response = requests.get(api_url).json()
        users = requests.get(base_url + "api/users").json()
        return response, users

    def get(self, request, project_id, task_id):
        response, users = self.get_object(project_id, task_id, request)
        context = {
            'task': response,
            'users': users,
            'project_id': project_id,
        }
        return render(request, self.template, context)

    def post(self, request, project_id, task_id):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task/{task_id}"
        print(api_url)
        payload = {
            "id": task_id,
            "name": request.POST['name'],
            "description": request.POST['description'],
            "start_date": request.POST['start_date'],
            "end_date": request.POST['end_date']
            # "assigned_to": request.POST['assigned_to']
        }

        requests.put(api_url, data=payload)
        return redirect('TaskDetail', project_id=project_id, task_id=task_id)


class TaskList(View):
    template = 'frontend/task_list.html'

    def get_object(self, project_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id):
        response = self.get_object(project_id, request)
        context = {
            'tasks': response,
            'project_id': project_id
        }
        return render(request, self.template, context)


class TaskDetail(View):
    template = 'frontend/task.html'

    def get_object(self, project_id, task_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task/{task_id}"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id, task_id):
        response = self.get_object(project_id, task_id, request)
        context = {
            'task': response,
            'project_id': project_id,

        }
        return render(request, self.template, context)


class SubTaskCreate(View):
    def post(self, request, project_id, task_id):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + \
            f"api/project/{project_id}/task/{task_id}/subtask/create"
        payload = {
            "name": request.POST['name']
        }
        requests.post(api_url, data=payload)
        return redirect('SubTaskList', project_id=project_id, task_id=task_id)


class SubTaskUpdate(View):
    template = 'frontend/subtask_form.html'

    def get_object(self, project_id, task_id, subtask_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + \
            f"api/project/{project_id}/task/{task_id}/subtask/{subtask_id}"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id, task_id, subtask_id):
        response = self.get_object(project_id, task_id, subtask_id, request)
        context = {
            'subtask': response,
            'task_id': task_id,
            'project_id': project_id,
        }
        return render(request, self.template, context)

    def post(self, request, project_id, task_id, subtask_id):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + \
            f"api/project/{project_id}/task/{task_id}/subtask/{subtask_id}"
        payload = {
            "id": task_id,
            "name": request.POST['name'],
            "description": request.POST['description'],
        }
        requests.put(api_url, data=payload)
        return redirect('SubTaskDetail', project_id=project_id, task_id=task_id, subtask_id=subtask_id)


class SubTaskList(View):
    template = 'frontend/subtask_list.html'

    def get_object(self, project_id, task_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + f"api/project/{project_id}/task/{task_id}/subtask"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id, task_id):
        response = self.get_object(project_id, task_id, request)
        context = {
            'subtasks': response,
            'project_id': project_id,
            'task_id': task_id,
        }
        return render(request, self.template, context)


class SubTaskDetail(View):
    template = 'frontend/subtask.html'

    def get_object(self, project_id, task_id, subtask_id, request):
        base_url = request.build_absolute_uri('/')
        api_url = base_url + \
            f"api/project/{project_id}/task/{task_id}/subtask/{subtask_id}"
        response = requests.get(api_url).json()
        return response

    def get(self, request, project_id, task_id, subtask_id):
        response = self.get_object(project_id, task_id, subtask_id, request)
        context = {
            'subtask': response,
            'project_id': project_id,
            'task_id': task_id,

        }
        return render(request, self.template, context)
