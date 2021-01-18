# -*- coding: utf-8 -*-
# Django
from django.db import models
# Python and Third Parties
import uuid
# Project
from entbook.utils.models import CommonModel


class Company(CommonModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    market_values = models.TextField(
        help_text="This field gonna be saved as a plain text in DB, "
                  "and it represents a list split by commas",
    )

    def __str__(self):
        return "{} | {}".format(self.pk, self.name)

    @property
    def market_values_list(self):
        if self.market_values:
            if self.market_values.endswith(","):
                self.market_values = self.market_values[:len(self.market_values ) - 1]
            market_values_list = self.market_values.split(",")
            return market_values_list
        return []

    class Meta:
        db_table = "companies"
        ordering = ['-created_on']
        verbose_name_plural = "Companies"
