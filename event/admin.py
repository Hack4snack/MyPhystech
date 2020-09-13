from django.contrib import admin

from .models import Event

# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'start_time', 'event_img_url', 'tags')
    fields = ['title', 'description', 'location', 'start_time', 'event_img_url', 'tags']
    list_filter = [('tags')]