from django.contrib import admin
from . models import Phons

# Register your models here.

@admin.register(Phons)
class PhonsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']