# -*- coding: utf-8 -*-
# Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("entbook.companies.urls", 'companies'), namespace="companies")),
]
