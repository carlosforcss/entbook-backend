# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework import serializers
# Project
from entbook.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "description",
            "symbol",
            "market_values",
            "market_values_list",
        )
