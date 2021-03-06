from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    in_print = models.BooleanField(default=True)


# Create your models here.
