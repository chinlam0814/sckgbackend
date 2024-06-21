from django.contrib import admin
from .models import Account, Admin

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'join_date', 'gender')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'join_date', 'gender')
