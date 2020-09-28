
import json
from django.core import serializers
from django.contrib.sessions.serializers import JSONSerializer, PickleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Profile, UserSession
# from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

from google.oauth2 import id_token
from google.auth.transport import requests


@api_view(['POST'])
def google_signup(req):
    token = req.GET.get('idToken')
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        CLIENT_ID = '942480069892-05kgachoktolijpd718lpna2smq6rsdk.apps.googleusercontent.com'
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo is not None:
            try:
                user = Profile.objects.get(email=idinfo['email'])
            except ObjectDoesNotExist:
                user = Profile.objects.create(email=idinfo['email'])
                user.save()

            if not req.session.exists(req.session.session_key):
                req.session.create()

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


# def authentication(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponse(True)
#     else:
#         return HttpResponse(False)


def update_profile(req):
    # session_key = req.session['session_key']
    # session = UserSession.objects.get(session=session_key)
    user = Profile.objects.get('email'==req.session['email'])
    user.profile.group = req.POST.get('group')
    user.save()


from django_mysql.models import ListF


@login_required
@api_view(['POST'])
def subscribe_tags(req):
    try:
        tags = [tag.strip() for tag in req.POST.get('tags').split(',')]
        session_key = req.session.session_key
        user = Profile.objects.get('email'==req.session['email'])
        for tag in tags:
            user.profile.subscribe_tags = ListF('subscribe_tags').append(tag)
        user.save()
        return HttpResponse(True)
    except Exception as e:
        return HttpResponse(e)


@login_required
@api_view(['POST'])
def subscribe_channels(req):
    channels = [channel.strip() for channel in req.POST.get('channels').split(',')]
    try:
        session_key = req.session['session_key']
        user = Profile.objects.get('email'==req.session['email'])
        for channel in channels:
            user.profile.subscribe_channels = ListF('subscribe_channels').append(channel)
        user.save()
        return HttpResponse(True)
    except Exception as e:
        return HttpResponse(e)


@login_required
@api_view(['POST'])
def schedule_tags(req):
    try:
        tags = [tag.strip() for tag in req.POST.get('tags').split(',')]
        session_key = req.session['session_key']
        user = Profile.objects.get('email'==req.session['email'])
        for tag in tags:
            user.profile.schedule_tags = ListF('schedule_tags').append(tag)
        user.save()
        return HttpResponse(True)
    except Exception as e:
        return HttpResponse(e)


@login_required
@api_view(['POST'])
def schedule_channels(req):
    channels = [channel.strip() for channel in req.POST.get('channels').split(',')]
    try:
        session_key = req.session['session_key']
        user = Profile.objects.get('email'==req.session['email'])
        for channel in channels:
            user.profile.schedule_channels = ListF('schedule_channels').append(channel)
        user.save()
        return HttpResponse(True)
    except Exception as e:
        return HttpResponse(e)

# @login_required
# @api_view(['GET'])
# def get_(req):
#     ids = [id for id in req.GET.get('id').split(',')]
#     print(ids)
#     latest_filtered_events = Event.objects.filter(id__in=ids).distinct()
#     serializer = EventUserSerializer(latest_filtered_events, many=True)
#     return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})




# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#         'auth': unicode(request.auth),  # None
#     }
#     return Response(content)

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return JsonResponse(request)

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
