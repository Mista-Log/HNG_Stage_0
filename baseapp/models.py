from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    email = models.CharField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    github_link = models.CharField(max_length=254)

    def __str__(self):
        return self.email







