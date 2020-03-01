import json
import re
import datetime as dt

from .models import Event
from taggit.models import Tag
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers

time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')

@api_view(['GET'])
def home(request):
    return HttpResponse('Hello world')


@api_view(['GET'])
def all_ev(request):
    es = Event.objects.all()
    data = serializers.serialize('json', es)
    return HttpResponse(data)


@api_view(['POST', 'PUT'])
def add_event(req):
    # print(req.POST)
    # print(req.body)
    data = json.loads(req.body.decode('utf8'))
    event = Event.objects.create(title=data['title'],
                  location=data['location'],
                  description=data['description'],
                  start_time=parse_time(data['start_time']),
                  end_time=parse_time(data['end_time']),
                  tags=data['tags'])
                  # user_id=int(data.['user_id']))
    res = event.save(commit=True)
    return HttpResponse(event.id)

def parse_time(str):
    if time_re.search(str):
        data = time_re.search(str)
        daytime = dt.datetime(**data.groupdict())
    else:
        daytime = None
    return daytime

# def get_events(req):
#     data = json.loads(req.body.decode('utf8'))
#     es = Event.objects.filter(id=data.userID,
#                               start_time=data.date,
#                               tags=)
#     data = serializers.serialize('json', es)
#     return HttpResponse(data)
