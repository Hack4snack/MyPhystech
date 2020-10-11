from django.urls import path
from . import views


urlpatterns = [
    path('random', views.random),
    path('tags', views.events_by_tags),
    path('channel/events', views.events_by_channel),
    path('channel', views.get_study_groups),
]

