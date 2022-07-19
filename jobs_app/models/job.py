from django.db import models
from django.db.models.deletion import CASCADE

class Job(models.Model):
    """
    Schema for jobs
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
