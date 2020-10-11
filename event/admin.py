from django.contrib import admin

from .models import Event

# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'start_time', 'event_img_url', 'tags', 'channel')
    fields = ['title', 'description', 'location', 'start_time', 'end_time', 'repeat_mode','event_img_url', 'tags', 'channel']
    list_filter = [('tags')]