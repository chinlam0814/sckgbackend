from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import FileInfo, UploadFile

@admin.register(FileInfo)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at', 'json_created')

@admin.register(UploadFile)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')