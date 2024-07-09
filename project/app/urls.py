
from django.urls import path
from .views import user,tasks
from .views import ex_u_xlsx, ex_t_xlsx

urlpatterns = [
    path('user/',user, name='user'),
    path('tasks/',tasks, name='tasks'),
    path('export-user/',ex_u_xlsx,name='export_user_xlsx'),
    path('export-tasks/',ex_t_xlsx,name='export_tasks_xlsx')
]
