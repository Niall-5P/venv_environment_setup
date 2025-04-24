# collaboration/admin.py
from django.contrib import admin
from .models import CollaborationRequest


@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'brand_name', 'email', 'submitted_at')
    list_filter   = ('submitted_at',)
    search_fields = ('full_name', 'brand_name', 'email')
