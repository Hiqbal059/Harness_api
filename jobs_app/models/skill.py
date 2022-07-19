# pylint: disable=missing-module-docstring
from django.db import models

class Skill(models.Model):
    """
    Schema for Skill
    """
    title = models.CharField(max_length=100, blank=False)
