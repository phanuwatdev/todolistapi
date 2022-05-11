from django.contrib import admin
from .models import Todolist

class TodolistTable(admin.ModelAdmin):
    list_display = ['id','created_date','update_date','task','checked','order','published']
    list_filter = ['published','checked']
    search_fileds = ['task']
    
# Register your models here.
admin.site.register(Todolist, TodolistTable)