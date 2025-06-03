from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()
    attendee_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def capacity_left(self):
        return self.max_capacity - self.attendee_count

    @property
    def capacity_reached(self):
        return self.attendee_count >= self.max_capacity


class Attendee(models.Model):
    event = models.ForeignKey(
        Event,
        related_name="attendees",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        unique_together = ("event", "email")

    def __str__(self):
        return f"{self.name} -- {self.email}"


@receiver(post_save, sender=Attendee)
def increment_attendee_count(sender, instance, created, **kwargs):
    if created and settings.SIGNAL_ENABLE:
        event = instance.event
        event.attendee_count += 1
        event.save(update_fields=["attendee_count"])


@receiver(post_delete, sender=Attendee)
def decrement_attendee_count(sender, instance, **kwargs):
    if settings.SIGNAL_ENABLE:
        event = instance.event
        event.attendee_count = max(0, event.attendee_count - 1)
        event.save(update_fields=["attendee_count"])
