"""RF-003: o sistema deve negar login a usuário inativo."""

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.models import Usuario
from api.serializers import MENSAGEM_LOGIN_INVALIDO


class LoginUsuarioInativoTests(APITestCase):
    SENHA = "senha-forte-123"
    EMAIL = "gestor@empresa.com"

    def setUp(self):
        self.url = reverse("login")
        self.usuario = Usuario.objects.create_user(
            self.EMAIL, self.SENHA, perfil=Usuario.Perfil.GESTOR
        )

    def _entrar(self, senha=None):
        return self.client.post(self.url, {"email": self.EMAIL, "password": senha or self.SENHA})

    def _inativar(self):
        self.usuario.is_active = False
        self.usuario.save()

    def test_inativo_com_credenciais_corretas_e_negado_como_credencial_invalida(self):
        invalida = self._entrar("errada")
        self._inativar()

        resposta = self._entrar()

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resposta.json(), invalida.json())
        self.assertEqual(resposta.json()["non_field_errors"], [MENSAGEM_LOGIN_INVALIDO])
        self.assertFalse(Token.objects.filter(user=self.usuario).exists())

    def test_token_antigo_de_usuario_inativado_e_recusado(self):
        # Não há rota autenticada além do login; status-api é AllowAny, mas o DRF
        # ainda valida o cabeçalho Token e recusa token de usuário inativo.
        token = self._entrar().json()["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        self.assertEqual(self.client.get(reverse("status-api")).status_code, status.HTTP_200_OK)

        self._inativar()

        self.assertEqual(
            self.client.get(reverse("status-api")).status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_reativar_usuario_volta_a_permitir_login(self):
        self._inativar()
        self.assertEqual(self._entrar().status_code, status.HTTP_400_BAD_REQUEST)

        self.usuario.is_active = True
        self.usuario.save()

        resposta = self._entrar()
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertIn("token", resposta.json())
