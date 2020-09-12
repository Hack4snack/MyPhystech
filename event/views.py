import json
import re
import datetime as dt

from .models import Event
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib.auth.decorators import login_required


time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')

@api_view(['GET'])
def home(request):
    return HttpResponse('Here exist some events')


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
    data = json.loads(req.read())
    # raise Exception((type(data), type(req.read()), data))
    event = Event.objects.create(**data)
    event.save()
    return HttpResponse(event.id)


@api_view(['GET'])
def last_events(req):
    latest_events_list = Event.objects.order_by('-start_time')[:5]
    return HttpResponse(latest_events_list)


@api_view(['GET'])
def filter_events_by_tags(req):
    tags = req.body
    latest_filtered_events = Event.objects.filter(tags__name__in=tags)
    return HttpResponse(latest_filtered_events)

@api_view(['GET'])
def get_events(req, offset, limit):
    offset, limit = int(offset), int(limit)
    es = Event.objects.all()[offset:offset+limit]
    with open('file.json', 'w', encoding='utf-8') as out:
        serializers.serialize('json', es, stream=out)
    with open('file.json', 'r', encoding='utf-8') as fd:
        data = json.load(fd)
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf8'))

@login_required
@api_view(['GET'])
def get_schedule(req):
    es = Events.objects.filter(tags__name__in=req.user.group_number)
    #serializers.serialize('json', es, stream=out)
    return HttpResponse('Holy Shit!')


# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return
