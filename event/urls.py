from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('all/', views.all_ev),
    path('add/', views.add_event),
    re_path(r'filter', views.filter_events_by_tags),
    re_path(r'events', views.get_events),
    re_path(r'schedule', views.get_schedule),
]

