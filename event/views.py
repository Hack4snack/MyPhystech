import json
import re
import datetime as dt

from .models import Event
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .serializers import EventSerializer


time_re = re.compile(r'^(?P<hours>\d\d):(?P<min>\d\d) (?P<day>\d+)-(?P<month>\d+)-(?P<year>\d{4})$')

@api_view(['GET'])
def home(request):
    return HttpResponse('Here exist some events')


@api_view(['GET'])
def all_ev(request):
    es = Event.objects.all()
    serializer = EventSerializer(es, many=True)
    # print(data)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST', 'PUT'])
def add_event(req):
    data = json.loads(req.read(), encoding='utf8')
    group = data.pop('group', None)
    data['group_img_url'] = group
    # raise Exception((type(data), type(req.read()), data))
    event = Event.objects.create(**data)
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
    print(tags)
    latest_filtered_events = Event.objects.filter(tags__name__in=tags).distinct()
    serializer = EventSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def get_events(req):
    offset, limit = int(req.GET.get('offset')), int(req.GET.get('limit'))
    es = Event.objects.all()[offset:offset+limit]
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


# @login_required
@api_view(['GET'])
def get_schedule(req):
    month = req.GET.get('month')
    es = Event.objects.filter(tags__name__in=req.GET.get('group'))
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def get_by_id(req):
    ids = [id for id in req.GET.get('id').split(',')]
    print(ids)
    latest_filtered_events = Event.objects.filter(id__in=ids).distinct()
    serializer = EventSerializer(latest_filtered_events, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


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
