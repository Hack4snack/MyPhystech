from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('all/', views.all_ev),
    path('add/', views.add_event),
    re_path(r'offset=(?P<offset>\d+)\&limit=(?P<limit>\d+)/', views.get_events),
    re_path(r'schedule?month=(?P<month>\w+)/', views.get_schedule),
]

