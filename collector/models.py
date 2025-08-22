# from django.db import models

# Create your models here.
# collector/models.py
from django.db import models
from django.utils import timezone

class Credential(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"