
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('signin', views.google_signup),
    path('signup', views.signup),
    path('logout', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('subscriptions/tags', views.subscribe_tags),
    path('subscriptions/channels', views.subscribe_channels),
    # path('schedule/tags', views.schedule_tags),
    path('schedule/channels', views.schedule_channels),
    path('feed', views.feed),
    path('schedule', views.schedule)
]
