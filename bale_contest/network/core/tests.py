from django.test import TestCase
from rest_framework import status 
from rest_framework.test import APIClient 


class TestCustomeUser(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate()


# No time for tests!