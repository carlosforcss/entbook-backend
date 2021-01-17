# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework import serializers
# Project
from entbook.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):

    @staticmethod
    def validate(name):
        if len(name) > 50:
            raise serializers.ValidationError("The name has to have less than 50 characters.")
        return name

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "description",
            "symbol",
        )
