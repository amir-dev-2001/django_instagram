from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _ 


class Location(models.Model):
    title = models.CharField(_("title"), max_length=32)
    points = JSONField(_("points")) # sample : {"lat": 48.826265, "long": 2.3262565}


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

        
        