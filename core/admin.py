from django.contrib import admin
from .models import Chefs
from unfold.admin import ModelAdmin

@admin.register(Chefs)
class ChefAdmin(ModelAdmin):
    list_display = ['name', 'position', 'created_at']