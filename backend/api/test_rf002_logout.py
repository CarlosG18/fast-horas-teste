from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.models import Usuario


class LogoutTests(APITestCase):
    SENHA = "senha-forte-123"

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            "gestor@empresa.com", self.SENHA, perfil=Usuario.Perfil.GESTOR
        )

    def _login(self):
        resposta = self.client.post(
            reverse("login"), {"email": "gestor@empresa.com", "password": self.SENHA}
        )
        return resposta.json()["token"]

    def test_logout_invalida_token_e_novo_login_restaura_acesso(self):
        token = self._login()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        resposta = self.client.post(reverse("logout"))

        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Token.objects.filter(user=self.usuario).exists())
        self.assertEqual(
            self.client.get(reverse("status-api")).status_code, status.HTTP_401_UNAUTHORIZED
        )

        self.client.credentials()
        novo = self._login()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {novo}")
        self.assertEqual(self.client.get(reverse("status-api")).status_code, status.HTTP_200_OK)

    def test_logout_sem_autenticacao_e_negado(self):
        resposta = self.client.post(reverse("logout"))

        self.assertEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_no_logout_retorna_405(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self._login()}")

        resposta = self.client.get(reverse("logout"))

        self.assertEqual(resposta.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
