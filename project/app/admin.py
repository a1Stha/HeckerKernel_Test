from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email','Mobile','ID','Task')  
admin.site.register(User,UserAdmin)


admin.site.register(Task)
