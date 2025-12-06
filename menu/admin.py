from django.contrib import admin
from .models import Category, Manls

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Manls)
class ManlsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']