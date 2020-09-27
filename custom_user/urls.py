
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('signin', views.google_signup),
    path('signup', views.signup),
    path('logout', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('subscribe_tags', views.subscribe_tags),
    path('subscribe_channels', views.subscribe_channels),
    path('schedule_tags', views.schedule_tags),
    path('schedule_channels', views.schedule_channels),
]
