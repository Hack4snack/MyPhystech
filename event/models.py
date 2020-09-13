import uuid

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # event_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    event_img_url = models.TextField(blank=True, null=True)
    group_img_url = models.TextField(blank=True, null=True)
    source_url = models.TextField(blank=True, null=True)

    repeat_mode = models.CharField(max_length=20, default='once')  # once_week once_2week once

    tags = TaggableManager()

    created_date = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, **kwargs):
        event = cls(**kwargs)
        event.tags.add(kwargs['tags'])
        return event

    class Meta:
        ordering = ["-start_time", "-created_date"]

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        s = "title: {}\n".format(self.title)
        s += "event_id: {}\n".format(self.event_id)
        s += "description: {}\n".format(self.description)
        s += "location: {}\n".format(self.location)
        s += "start_time: {}\n".format(self.start_time)
        s += "end_time: {}\n".format(self.end_time)
        s += "event_img_url: {}\n".format(self.event_img_url)
        s += "group_img_url: {}\n".format(self.group_img_url)
        s += "repeat_mode: {}\n".format(self.repeat_mode)
        return s


# # class EventInstance(models.Model):
# #     event_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
# #     event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
# #
# #     created_date = models.DateTimeField(default=timezone.now)
#
#     @classmethod
#     def create(cls, **kwargs):
#         event = cls(**kwargs)
#         event.tags.add(kwargs['tags'])
#         return event
#
#     class Meta:
#         ordering = ["-start_time", "-created_date"]
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#
#     # def publish(self):
#     #     self.published_date = timezone.now()
#     #     self.save()
#
#     def publish(self):
#         self.created_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         s = "title: {}\n".format(self.title)
#         s += "event_id: {}\n".format(self.event_id)
#         s += "description: {}\n".format(self.description)
#         s += "location: {}\n".format(self.location)
#         s += "start_time: {}\n".format(self.start_time)
#         s += "end_time: {}\n".format(self.end_time)
#         s += "event_img_url: {}\n".format(self.event_img_url)
#         s += "group_img_url: {}\n".format(self.group_img_url)
#         s += "repeat_mode: {}\n".format(self.repeat_mode)
#         return s

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group_number = models.TextField(max_length=10)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()











