

from rest_framework.generics import ListCreateAPIView
from .models import Event, Attendee
from events.serializers import EventSerializer, AttendeeSerializer
from django.utils import timezone
from event_management_system.response import SuccessResponseMixin, SuccessResponse
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.decorators import action


class EventListCreateView(SuccessResponseMixin, ListCreateAPIView):
    serializer_class = EventSerializer
    model_name = "Event"
    http_method_names = ['get', 'post']

    def get_queryset(self):

        return Event.objects.filter(
            start_time__gte=timezone.now(),
        ).order_by("start_time")


class EventAttendeeViewSet(GenericViewSet, ListModelMixin):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        event_id = self.kwargs.get("event_id")
        return Attendee.objects.filter(event_id=event_id).order_by("name")

    @action(detail=True, methods=["post"], url_path="register")
    def register(self, request, event_id=None):
        serializer = self.get_serializer(
            data=request.data, context={"event_id": event_id}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessResponse(data=serializer.data,status_code=201)
