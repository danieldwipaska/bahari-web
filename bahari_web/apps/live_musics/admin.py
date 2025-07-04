from django.contrib import admin
from .models import LiveMusic


@admin.register(LiveMusic)
class LiveMusicAdmin(admin.ModelAdmin):
    list_display = ("name", "schedule", "is_active")
    list_filter = ("created_at",)
    search_fields = ("name", "description", "schedule")
    readonly_fields = ("created_at", "updated_at")
