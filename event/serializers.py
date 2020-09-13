from rest_framework import serializers
from event.models import Event
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class EventSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Event
        fields = ['title', 'description',
                  'location', 'start_time',
                  'event_img_url', 'group_img_url',
                  'source_url', 'repeat_mode']
