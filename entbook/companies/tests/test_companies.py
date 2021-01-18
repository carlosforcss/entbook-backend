# -*- coding: utf-8 -*-
# Django
from django.test import Client
# Third Parties
from faker import Faker
# Project
from entbook.companies.models import Company
from entbook.utils.tests import TestCase


class CompanyTest(TestCase):

    BASE_URL = "/api/company/"

    def get_company_data(self):
        data = dict(
            name=self.faker.name(),
            description=self.get_text(max_nb_chars=50),
            symbol=self.get_text(max_nb_chars=10),
            market_values="{}, {}, {},".format(self.faker.name(), self.faker.name(), self.faker.name())
        )
        return data

    def test_create_company(self):
        data = self.get_company_data()
        response = self.client.post(self.BASE_URL, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data.get("id"))

    def test_create_company_with_wrong_data(self):
        # Test too long fields
        fields = (
            ("name", 50),
            ("description", 100),
            ("symbol", 10),
        )
        for field_name, max_length in fields:
            data = self.get_company_data()
            data[field_name] = self.get_text(min_nb_chars=max_length)
            response = self.client.post(self.BASE_URL, data)
            message = "The field {} has saved with a too long size ({}).".format(field_name, max_length)
            self.assertEqual(response.status_code, 400, message)
            self.assertTrue(response.data.get(field_name), message)
