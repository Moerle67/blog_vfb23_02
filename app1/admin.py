from django.contrib import admin

from .models import *

# Register your models here.

# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['header', 'author', 'written', 'changed']
    list_filter = ['author', 'rating']
    search_fields = ['header', 'contents']
