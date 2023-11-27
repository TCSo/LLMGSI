from django.contrib import admin

# Register your models here.
from .models import LLMRequest

@admin.register(LLMRequest)
class GHAdmin(admin.ModelAdmin):
    ordering = ('-updated_at',)
    list_display = ['code','succeed','updated_at']