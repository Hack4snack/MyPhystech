import json
import re
import datetime as dt

from .models import Event
from custom_user.models import Profile, UserSession
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .serializers import EventSerializer, EventUserSerializer


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


@api_view(['POST', 'PUT'])
def add_event(req):
    data = json.loads(req.read(), encoding='utf8')
    tags = data.pop('tags', None)
    # raise Exception((type(data), type(req.read()), data))
    event = Event.objects.create(**data)
    event.tags.add(*tags)
    event.save()
    return HttpResponse(event.event_id)


@api_view(['GET'])
def last_events(req):
    latest_events_list = Event.objects.order_by('-start_time')[:5]
    serializer = EventSerializer(latest_events_list, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def filter_events_by_tags(req):
    tags = [tag.strip() for tag in req.GET.get('tags').split(',')]
    latest_filtered_events = Event.objects.filter(tags__name__in=tags).distinct()
    serializer = EventSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@login_required
@api_view(['GET'])
def get_events(req):
    offset, limit = int(req.GET.get('offset')), int(req.GET.get('limit'))
    session_key = req.session['session_key']
    session = UserSession.objects.get(session=session_key)
    user = session.user
    es = Event.objects.filter(tags__name__in=user.subscribe_tags)[offset:offset+limit]
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@login_required
@api_view(['GET'])
def get_schedule(req):
    session_key = req.session['session_key']
    session = UserSession.objects.get(session=session_key)
    user = session.user
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