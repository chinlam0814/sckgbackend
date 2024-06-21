from django.contrib import admin
from .models import Texts

@admin.register(Texts)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'created_at', 'json_created')
