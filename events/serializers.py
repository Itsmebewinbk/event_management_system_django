from rest_framework import serializers
from events.models import Event, Attendee


def required_fields_validation(required_fields, data):
    for field in required_fields:
        if not data.get(field):
            raise serializers.ValidationError({field: f"{field} is required."})
    return True


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "location",
            "start_time",
            "end_time",
            "max_capacity",
        )

    def validate(self, data):

        required_fields = (
            "name",
            "location",
            "start_time",
            "end_time",
            "max_capacity",
        )
        required_fields_validation(required_fields, data)

        if data["end_time"] <= data["start_time"]:
            raise serializers.ValidationError(
                "end_time must be after start_time",
            )
        existing_event = Event.objects.filter(
            name=data["name"],
            location=data["location"],
            start_time=data["start_time"],
            end_time=data["end_time"],
        )

        if self.instance:
            existing_event = existing_event.exclude(pk=self.instance.pk)

        if existing_event.exists():
            raise serializers.ValidationError(
                "An event with the same name, location, start time, and end time already exists."
            )
        return data


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ("id", "name", "email")

    def validate(self, data):
        self.event_id = self.context.get("event_id")
        try:
            event = Event.objects.get(id=self.event_id)
        except Event.DoesNotExist:
            raise serializers.ValidationError("Event does not exist.")

        required_fields = (
            "name",
            "email",
        )
        required_fields_validation(required_fields, data)

        if event.capacity_reached:
            raise serializers.ValidationError("Event is fully booked")

        if Attendee.objects.filter(
            event_id=self.event_id,
            email=data.get("email"),
        ).exists():
            raise serializers.ValidationError(
                "The email is already registered for the event"
            )
        return data

    def create(self, validated_data):

        return Attendee.objects.create(event_id=self.event_id, **validated_data)
