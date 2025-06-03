from django.contrib import admin
from .models import Event, Attendee

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "start_time",
        "end_time",
        "max_capacity",
        "attendee_count",
        "capacity_left",
        "capacity_reached",
        "created_at",
        "updated_at",
    )
    list_filter = ("start_time", "location")
    search_fields = ("name", "location")
    readonly_fields = ("attendee_count", "capacity_left", "capacity_reached", "created_at", "updated_at")

    def capacity_left(self, obj):
        return obj.capacity_left
    capacity_left.short_description = "Capacity Left"

    def capacity_reached(self, obj):
        return obj.capacity_reached
    capacity_reached.boolean = True
    capacity_reached.short_description = "Capacity Reached"


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event", "created_at", "updated_at")
    list_filter = ("event",)
    search_fields = ("name", "email")
    readonly_fields = ("created_at", "updated_at")
