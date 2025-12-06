from django.contrib import admin
from .models import Profile
from unfold.admin import ModelAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'date', 'guests', 'time', 'special_requests']