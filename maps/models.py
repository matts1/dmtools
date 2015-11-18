from django.conf import settings
from django.db import models


class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('Map')


class Map(Point):
    image = models.ImageField(upload_to='maps')
    root = models.BooleanField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def maps(self):
        raise NotImplementedError

    @property
    def characters(self):
        raise NotImplementedError

    def __unicode__(self):
        return self.name
