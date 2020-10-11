
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse, JsonResponse

from .models import Channel
from .serializers import ChannelSerializer
from event.models import Event
from event.serializers import EventSerializer
from taggit.models import Tag
import random as rd


@api_view(['GET'])
def random(req):
    channels = [channel.name for channel in Channel.objects.all()]
    tag_names = [tag.name for tag in Tag.objects.all()]
    randoms = rd.sample(tag_names, 5)
    randoms += rd.sample(channels, 5)
    return JsonResponse({'randoms': randoms}, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def events_by_tags(req):
    tags = [tag.strip() for tag in req.GET.get('tags').split(',')]
    latest_filtered_events = Event.objects.filter(tags__name__in=tags).distinct()
    serializer = EventSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def events_by_channel(req):
    tags = [tag.strip() for tag in req.GET.get('channelId').split(',')]
    latest_filtered_events = Event.objects.filter(tags__name__in=tags).distinct()
    serializer = EventSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def get_study_groups(req):
    channels = Channel.objects.filter(is_study_group=True)
    serializer = ChannelSerializer(channels, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})