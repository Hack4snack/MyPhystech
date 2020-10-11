from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('all/', views.all_ev),
    path('add', views.add_event),
    # path('events', views.get_events),
    path('by_id', views.get_by_id),
    path('schedule', views.get_schedule),
    path('search', views.search),
    path('feed', views.feed),
    path('likes', views.likes),
]

