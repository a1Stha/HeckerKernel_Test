# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from tablib import Dataset

from .forms import *
from .resources import UserResource, TaskResource


# Create your views here.


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url_name') 
    else:
        form = UserForm()
    return render(request,'app/user.html', {'form': form})

def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return ('task_added_successfully') 
    else:
        form = TaskForm()
    return render(request, 'app/task.html', {'form': form})






#  data to excel  User

def ex_u_xlsx(request):
    user_resource = UserResource()
    dataset = user_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xlsx"'
    return response


 #  data to excel for task



def ex_t_xlsx(request):
    task_resource = TaskResource()
    dataset = task_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tasks.xlsx"'
    return response