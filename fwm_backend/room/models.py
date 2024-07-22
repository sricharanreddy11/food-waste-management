from django.contrib.auth.models import User
from django.db import models


# class RoomQuerySet(models.QuerySet):
#     pass
#
#
# class RoomManager(models.Manager):
#     def get_queryset(self):
#         return RoomQuerySet(self.model, using=self._db)
#
#
# class Room(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#
#     objects = RoomManager()
#
