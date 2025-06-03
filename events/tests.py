from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from events.models import Event


class EventListCreateViewTest(TestCase):
    def setUp(self):
        self.url = reverse("event-list-create")

    def test_get_upcoming_events(self):

        Event.objects.create(
            name="Past Event",
            location="India",
            start_time=timezone.now() - timedelta(days=10),
            end_time=timezone.now() - timedelta(days=9),
            max_capacity=10,
        )

        response = self.client.get(self.url)
        print("response", response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventAttendeeViewSetTest(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name="Test Event",
            location="India",
            start_time=timezone.now() + timedelta(days=1),
            end_time=timezone.now() + timedelta(days=2),
            max_capacity=5,
        )
        self.register_url = reverse("event-attendee-register", args=[self.event.id])

    def test_register_attendee_success(self):
        data = {"name": "John Doe", "email": "john@example.com"}
        response = self.client.post(
            self.register_url, data, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        resp_data = response.json()
        self.assertEqual(resp_data.get("status"), "ok")
        self.assertEqual(resp_data.get("data")["email"], data["email"])
