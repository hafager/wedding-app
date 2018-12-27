from django.contrib import admin

# Register your models here.
from .models import Page

@admin.register(Page)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'hidden')
    list_editable = ('hidden',)
