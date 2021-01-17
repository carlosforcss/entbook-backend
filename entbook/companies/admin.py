# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django
from django.contrib import admin
# Python and third parties
# - - -
# Project
from entbook.companies.models import Company

admin.site.register(Company)
