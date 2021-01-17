# -*- coding: utf-8 -*-
# Django
from django.urls import path, include
# Third Parties
from rest_framework import routers
# Project
from entbook.companies.views import CompanyViewSet


router = routers.DefaultRouter()
router.register('company', CompanyViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
