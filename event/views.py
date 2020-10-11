import json
import re
import datetime as dt

from .models import Event, Like
from .serializers import EventSerializer, EventUserSerializer

from topics.models import Channel
from topics.serializers import ChannelSerializer

from custom_user.models import Profile
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

# from taggit import Tag
from taggit_serializer.serializers import TaggitSerializer

from custom_user.accounts_helpers import get_user_by_token


time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')


@api_view(['GET'])
def home(request):
    return HttpResponse('Here is home for MyPhystech')


@api_view(['GET'])
def all_ev(request):
    es = Event.objects.all()
    serializer = EventSerializer(es, many=True)
    # print(data)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def add_event(req):
    data = json.loads(req.read(), encoding='utf8')
    tags = data.pop('tags', None)
    channel_data = data.pop('channel_data')
    channel = Channel.objects.filter(title=channel_data['title']).first()
    if channel is None:
        channel = Channel.objects.create(**channel_data)

    event = Event.objects.create(**data, channel=channel.id)
    if 'repeat_mode' in data:
        parent = event
        res = data.pop('repeat_mode')
        for i in range(res):
            child = Event.objects.create(**data, channel=channel.id)
            child.parent_id = parent.id
    else:
        event.parent_id = event.id

    if tags is not None:
        event.tags.add(*tags)
    event.save()
    return HttpResponse(event.event_id)


@api_view(['GET'])
def last_events(req):
    latest_events_list = Event.objects.order_by('-start_time')[:5]
    serializer = EventSerializer(latest_events_list, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@login_required
@api_view(['GET'])
def feed(req):
    offset, limit = int(req.GET.get('offset')), int(req.GET.get('limit'))
    email = req.session['email']
    user = Profile.objects.get(email=email)
    if user is None:
        return JsonResponse({[]})
    es = Event.objects.all()[offset:offset+limit]
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def get_all_events(req):
    offset, limit = int(req.GET.get('offset')), int(req.GET.get('limit'))
    es = Event.objects.all()[offset:offset+limit]
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


# @login_required
@api_view(['GET'])
def get_schedule(req):
    token = req.GET.get('idToken')
    user = get_user_by_token(token)
    if user is None:
        return JsonResponse({[]})
    es = Event.objects.filter(channel__in=user.scheduled_channels)
    serializer = EventUserSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def get_by_id(req):
    ids = [id for id in req.GET.get('id').split(',')]
    print(ids)
    latest_filtered_events = Event.objects.filter(id__in=ids).distinct()
    serializer = EventUserSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST', 'DELETE'])
def likes(req):
    if req.method == 'POST':
        eid = req.POST.get('eventId')
        event = Event.objects.get(pk=eid)
        event.likes += 1
        user = Profile.objects.get(email=req.session['email'])
        Like.objects.create(user_id=user.id, event_id=eid)
    elif req.method == 'DELETE':
        eid = req.DELETE.get('eventId')
        event = Event.objects.get(pk=eid)
        event.likes -= 1
        user = Profile.objects.get(email=req.session['email'])
        Like.objects.get(user_id=user.id, event_id=eid).delete()



@api_view(['GET'])
def search(req):
    text = req.GET.get('text')
    data = {}

    chs = Channel.objects.filter(title__in=text)
    chSer = ChannelSerializer(chs, many=True)
    data['channels'] = chSer.data

    evs = Event.objects.filter(description__in=text)
    evSer = EventSerializer(evs, many=True)
    data['events'] = evSer.data

    # tgs = Tag.object.filter(slug__in=text)
    # tgSer = TaggitSerializer(tgs, many=True)
    # data['tags'] = tgSer.data

    data['autosuggest'] = ''

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


