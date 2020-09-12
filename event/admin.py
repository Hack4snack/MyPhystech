from django.contrib import admin

from .models import Event
# Register your models here.

# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'start_time', 'event_img_url')
    fields = ['title', 'description', 'location', 'start_time', 'event_img_url']
    list_filter = [('tags')]