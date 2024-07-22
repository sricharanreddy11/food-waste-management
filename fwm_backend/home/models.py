from django.db import models
from django.contrib.auth.models import User


class ContributionQuerySet(models.QuerySet):
    pass


class ContributionManager(models.Manager):
    def get_queryset(self):
        return ContributionQuerySet(self.model, using=self._db)


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    donor_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    address = models.TextField(null=False)
    people = models.IntegerField(default=10)
    requests = models.IntegerField(default=0)

    objects = ContributionManager()

    class Meta:
        ordering = ["-people"]
