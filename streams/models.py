from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

class LocationTag(models.Model):
    tag = models.CharField(max_length=100, blank=False, null=False, help_text="location tag")

    panels = [
                FieldPanel("tag"),
            ]

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Location Tag"
        verbose_name_plural = "Location Tags"

register_snippet(LocationTag)

class TripType(models.Model):
    trip_type = models.CharField(max_length=100, blank=False, null=False, help_text="location tag")

    panels = [
                FieldPanel("trip_type"),
            ]

    def __str__(self):
        return self.trip_type

    class Meta:
        verbose_name = "Trip Type"
        verbose_name_plural = "Trip Types"

register_snippet(TripType)
