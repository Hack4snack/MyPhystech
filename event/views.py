import json
import re
import os
import datetime as dt

from .models import Event
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
from simplejson import dumps

time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')

@api_view(['GET'])
def home(request):
    return HttpResponse('Hello world')


@api_view(['GET'])
def all_ev(request):
    es = Event.objects.all()
    with open('file.json', 'w', encoding='utf-8') as out:
        serializers.serialize('json', es, stream=out)
    with open('file.json', 'r', encoding='utf-8') as fd:
        data = json.load(fd)
    # print(data)
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf8'))


@api_view(['POST', 'PUT'])
def add_event(req):
    # print(req.POST)
    print(req.body.decode('utf8'))
    data = json.loads(req.body.decode('utf8'))
    event = Event.objects.create(
                  title=data['title'],
                  location=data['location'],
                  description=data['description'],
                  start_time=dt.datetime.strptime(data['start_time'], '%H:%M %d.%m.%Y'),
                  # end_time=dt.datetime.strptime(data['end_time'], '%H:%M %d-%m-%Y'),
                  tags=data['tags'],
                  img_url=data['img_url'])
                  # user_id=int(data.['user_id']))
    res = event.save()
    return HttpResponse(event.id)


@api_view(['GET'])
def last_events(req):
    latest_events_list = Event.objects.order_by('-start_time')[:5]
    return HttpResponse(latest_events_list)


@api_view(['GET'])
def filter_events_by_tags(req):
    tags = req.body
    latest_filtered_events = Event.objects.filter(tags)
    return HttpResponse(latest_filtered_events)

