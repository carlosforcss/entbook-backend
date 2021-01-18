# -*- coding: utf-8 -*-
# Django
from django.views import View
from django.shortcuts import render
# Third Parties
from rest_framework import viewsets
# Project
from entbook.companies.models import Company
from entbook.companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListAndCreateView(View):
    template = "companies/list_and_create.html"

    def get(self, request):
        return render(request, self.template)
