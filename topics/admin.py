from django.contrib import admin

from .models import Channel

# admin.site.register(Event)
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_url', 'source_url', 'is_study_group')
    fields = ['title', 'img_url', 'source_url', 'is_study_group']
    list_filter = [('title')]