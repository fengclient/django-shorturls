# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Link(models.Model):
    shorten = models.CharField(max_length=8, null=False)
    expand = models.TextField(null=False)

