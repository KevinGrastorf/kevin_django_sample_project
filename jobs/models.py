from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='url')

    def __str__(self):
        return self.summary