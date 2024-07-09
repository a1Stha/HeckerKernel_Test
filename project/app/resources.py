
from import_export import resources
from .models import User, Task

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task
