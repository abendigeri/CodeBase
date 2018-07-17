# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Investment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    returns = models.FloatField(default=0.0)
    risk = models.FloatField(default=0.0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
