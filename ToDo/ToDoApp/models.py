from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
