from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Person Model"""

    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    birthday = models.DateField(blank=False, null=True)
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=256)
    skype = models.CharField(max_length=256)
    contacts = models.TextField()
    photo = models.ImageField(upload_to='photo', default='')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class AllRequest(models.Model):
    """Model for write to DB requests"""

    date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=256)
    cookies_dict = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.date, self.url)
