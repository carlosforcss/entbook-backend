# -*- coding: utf-8 -*-
# Django
from django.db import models
# Third Parties
# - - -


class CommonModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
