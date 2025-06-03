from django.urls import path
from .views import EventListCreateView, EventAttendeeViewSet



urlpatterns = [
    path("", EventListCreateView.as_view(), name="event-list-create"),
    path(
        "/<int:event_id>/attendees/",
        EventAttendeeViewSet.as_view(
            {
                "get": "list",
            }
        ),
        name="event-attendee-list",
    ),
    path(
        "/<int:event_id>/register/",
        EventAttendeeViewSet.as_view({"post": "register"}),
        name="event-attendee-register",
    ),
]
