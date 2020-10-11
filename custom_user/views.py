
import json
# from django.contrib.sessions.serializers import JSONSerializer, PickleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from django_mysql.models import ListF
from django.db.models import Q
from .models import Profile
from event.models import Event
from event.serializers import EventSerializer
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField
#from topics.models import Channel

# from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

from .accounts_helpers import verify_token


@api_view(['POST'])
def google_signup(req):
    token = req.GET.get('idToken')
    try:
        idinfo = verify_token(token)

        if idinfo is not None:
            try:
                user = Profile.objects.get(email=idinfo['email'])
            except ObjectDoesNotExist:
                user = Profile.objects.create(email=idinfo['email'])
                user.save()

            login(req, user, backend='social_core.backends.google.GoogleOAuth2')

            # if not req.session.exists(req.session.session_key):
            #     req.session.create()

            if user is not None:
                req.session['username'] = idinfo['name']
                req.session['email'] = idinfo['email']
                req.session['success_login'] = 'True'
            else:
                req.session['success_login'] = 'False'

            # serializer = JSONSerializer()
            # data = serializer.dumps(req.session)
            data = {'token': req.session.session_key}
            return JsonResponse(data)

    except Exception as e:
        raise e


from .forms import SignUpForm


@api_view(['POST'])
def signup(req):
    # print(req.read())
    data = json.loads(req.read(), encoding='utf8')
    form = SignUpForm(data)
    print(form.is_valid())
    if form.is_valid():
        profile = form.save()
        profile.refresh_from_db()  # load the profile instance created by the signal
        profile.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=profile.username, password=raw_password)
        if user is not None:
            login(req, user)
        return HttpResponse(req.session.session_key)
    else:
        return HttpResponse()


def update_profile(req):
    # session_key = req.session['session_key']
    # session = UserSession.objects.get(session=session_key)
    user = Profile.objects.get('email'==req.session['email'])
    user.profile.group = req.POST.get('group')
    user.save()


@login_required
@api_view(['GET', 'POST', 'DELETE'])
def subscribe_tags(req):
    user = req.session.user
    if user is None:
        return HttpResponse('User not found')
    if req.method == "POST":
        tags = [tag.strip() for tag in req.POST.get('tags').split(',')]
        for tag in tags:
            t = Tag.objects.get(name=tag)
            user.subscribe_tags.add(t)
        user.save()
        return HttpResponse(True)
    elif req.method == 'GET':
        data = TagListSerializerField(user.subscribe_tags, many=True, read_only=True)
        return JsonResponse({'subscribe_tags':data}, json_dumps_params={'ensure_ascii': False})
    elif req.method == 'DELETE':
        tags = [tag.strip() for tag in req.DELETE.get('tags').split(',')]
        for tag in tags:
            user.subscribe_tags.remove(tag)


@login_required
@api_view(['GET', 'POST', 'DELETE'])
def subscribe_channels(req):
    user = req.session.user
    if user is None:
        return HttpResponse('User not found')
    if req.method == "POST":
        channels = [channel.strip() for channel in req.POST.get('channels').split(',')]
        for channel in channels:
            user.subscribe_channels = ListF('subscribe_channels').append(channel)
        user.save()
        return HttpResponse(True)
    elif req.method == 'GET':
        data = [ch.title for ch in user.subscribe_channels]
        return JsonResponse({'subscribe_channels': data}, json_dumps_params={'ensure_ascii': False})
    elif req.method == 'DELETE':
        channels = [channel.strip() for channel in req.DELETE.get('channels').split(',')]
        for channel in channels:
            user.subscribe_channels = ListF('subscribe_channels').pop(channel)


@login_required
@api_view(['GET', 'POST', 'DELETE'])
def schedule(req):
    email = req.session['email']
    user = Profile.objects.get(email=email)
    if user is None:
        return HttpResponse('User not found')
    if req.method == 'GET':
        month = req.GET.get('month')
        # НЕПОНЯТНО БУДЕТ ЛИ РАБОТАТЬ
        events = Event.objects.filter(start_time__month=month & (Q(channel__in=user.scheduled_channels) | Q(event_id__in=user.scheduled_events))).exclude(parent_id__in=user.ignore_list)
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False})
    elif req.method == 'DELETE':
        evid = req.DELETE.get('eventId')
        event = Event.objects.get(id=evid)
        user.ignore_list = ListF('ignore_list').append(event.parent_id)
        if event.parent_id in user.scheduled_events:
            user.scheduled_events = ListF('scheduled_events').remove(evid)
    elif req.method == 'POST':
        chid = req.POST.get('channelId')
        evid = req.POST.get('eventId')
        user.scheduled_channels = ListF('scheduled_channels').append(chid)
        user.scheduled_events = ListF('scheduled_events').append(evid)


# @login_required
# @api_view(['GET', 'POST', 'DELETE'])
# def schedule_tags(req):
#     user = req.session.user
#     if user is None:
#         return HttpResponse('User not found')
#     if req.method == 'POST':
#         tags = [tag.strip() for tag in req.POST.get('tags').split(',')]
#         user.schedule_tags.add(tags)
#         user.save()
#         return HttpResponse(True)
#     elif req.method == 'GET':
#         data = TagListSerializerField(user.schedule_tags, many=True, read_only=True)
#         return JsonResponse({'schedule_tags': data}, json_dumps_params={'ensure_ascii': False})
#     elif req.method == 'DELETE':
#         tags = [tag.strip() for tag in req.DELETE.get('tags').split(',')]
#         for tag in tags:
#             user.schedule_tags.remove(tag)


@login_required
@api_view(['GET', 'POST', 'DELETE'])
def schedule_channels(req):
    user = req.session.user
    if user is None:
        return HttpResponse('User not found')

    if req.method == 'POST':
        channels = [channel.strip() for channel in req.POST.get('channels').split(',')]
        for channel in channels:
            user.schedule_channels = ListF('schedule_channels').append(channel)
        user.save()
        return HttpResponse(True)
    elif req.method == 'GET':
        data = user.schedule_channels
        return JsonResponse({'schedule_channels': data}, json_dumps_params={'ensure_ascii': False})
    elif req.method == 'DELETE':
        channels = [channel.strip() for channel in req.DELETE.get('channels').split(',')]
        for channel in channels:
            user.schedule_channels = ListF('schedule_channels').pop(channel)


@login_required
@api_view(['GET'])
def feed(req):
    user = req.session.user
    if user is None:
        return HttpResponse('User not found')
    offset, limit = int(req.GET.get('offset')), int(req.GET.get('limit'))
    user = req.session.user
    es = Event.objects.filter(tags__name__in=user.subscribe_tags)[offset:offset+limit]
    if es is None:
        es = Event.objects.all()[offset:offset+limit]
    serializer = EventSerializer(es, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})