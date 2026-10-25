from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class StatusApiTests(APITestCase):
    def test_status_retorna_ok(self):
        resposta = self.client.get(reverse("status-api"))

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.json(), {"status": "ok"})
