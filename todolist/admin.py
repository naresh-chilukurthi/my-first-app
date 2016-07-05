from django.contrib import admin

# Register your models here.
import todolist.models
admin.site.register(todolist.models.Todoitem)
admin.site.register(todolist.models.Todolist)