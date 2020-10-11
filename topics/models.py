from django.db import models
from django.utils import timezone


class Channel(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    source_url = models.TextField(blank=True, null=True)
    is_study_group = models.BooleanField(default=0)

    created_date = models.DateTimeField(default=timezone.now)

#  НЕ ВЫЗЫВАЕТСЯ ХЗ почему
    # @classmethod
    # def create(cls, **kwargs):
    #     event = cls(**kwargs)
    #     event.tags.add(kwargs['tags'])
    #     return event

    class Meta:
        ordering = ["title"]

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        s = "title: {}\n".format(self.title)
        s += "img_url: {}\n".format(self.img_url)
        s += "source_url: {}\n".format(self.source_url)
        s += "is_study_group: {}\n".format(bool(self.is_study_group))

        return s
