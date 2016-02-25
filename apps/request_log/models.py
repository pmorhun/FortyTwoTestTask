from django.db import models
from django.utils import timezone


class RequestsLog(models.Model):
    PRIORITY = (
        (0, 'Priority 0'),
        (1, 'Priority 1'),
    )
    created = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=20)
    path = models.CharField(max_length=254)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.created, self.method, self.path, self.priority)
