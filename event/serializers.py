from rest_framework import serializers
from event.models import Event
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

import six


class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)
        return value


class EventSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description',
                  'location', 'start_time',
                  'event_img_url', 'group_img_url',
                  'source_url', 'repeat_mode', 'tags']

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = serializers.ModelSerializer.create(validated_data)
        instance.tags.set(*tags)
        return instance
