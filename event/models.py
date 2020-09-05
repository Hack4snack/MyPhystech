import json

from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

from django.core import serializers


class Event(models.Model):
    title = models.CharField(max_length=80, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    # time_str = models.CharField(max_length=10, blank=True, null=True)
    event_img_url = models.TextField(blank=True, null=True)
    group_img_url = models.TextField(blank=True, null=True)
    source_url = models.TextField(blank=True, null=True)

    repeat_mode = models.CharField(max_length=20, null=True)  # once_week once_2week once

    tags = TaggableManager()

    created_date = models.DateTimeField(default=timezone.now)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

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

