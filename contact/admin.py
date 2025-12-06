from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contact

@admin.register(Contact)
class PupleAdmin(ModelAdmin):
    list_display = ('name',)


