# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework import viewsets
# Project
from entbook.companies.models import Company
from entbook.companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
