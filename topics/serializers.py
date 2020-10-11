from rest_framework import serializers
from .models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['title', 'img_url',
                  'source_url', 'is_study_group']