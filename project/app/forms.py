from django import forms

from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'Mobile','Task']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields ='__all__'
