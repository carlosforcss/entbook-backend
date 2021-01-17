# -*- coding: utf-8 -*-
# Django
from django.test import TestCase as DjangoTestCase, Client
# Third Parties
from faker import Faker


def _faker_needed(func):
    def decorator(self, *args, **kwargs):
        if not self.faker:
            raise Exception("You need to define a faker instance in your test.")
        return func(self, *args, **kwargs)
    return decorator


class TestCase(DjangoTestCase):

    """
        Base test class, you should use this in evry test you do in the project.

        This works equal to a TestCase calss, but you should use set_up method instead
        setUp method.
    """

    def setUp(self):
        """ You should not overwrite this """
        self.faker = Faker()
        self.client = Client()
        set_up = getattr(self, "set_up", None)
        if set_up:
            self.set_up()

    @_faker_needed
    def get_text(self, min_nb_chars=None, max_nb_chars=None):
        """
            A way to get an specific number of chars in faker doesn't exist,
            and this function works to be shure about the minimum number of chars
            withing a text.
        """
        max_nb_chars = min_nb_chars + 100 if min_nb_chars else max_nb_chars
        text = self.faker.text() if not max_nb_chars else self.faker.text(max_nb_chars=max_nb_chars)
        if min_nb_chars and len(text) < min_nb_chars:
            return self.get_text(min_nb_chars=min_nb_chars, max_nb_chars=max_nb_chars)
        return text
