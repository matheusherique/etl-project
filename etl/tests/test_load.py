from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class LoadTestCase(TestCase):

    def test_get_method(self):
        response = client.get(
            reverse('Load'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
