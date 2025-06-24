from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "created_at", "updated_at")
    list_filter = ("start_date", "end_date", "created_at")
    search_fields = ("name", "description")
    date_hierarchy = "start_date"
    readonly_fields = ("created_at", "updated_at")
