from django.contrib.auth.models import AbstractUser

from maps.models import Map


class User(AbstractUser):
    @property
    def campaigns(self):
        return Map.objects.filter(owner=self, root=True).order_by('name')