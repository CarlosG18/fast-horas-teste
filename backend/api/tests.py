from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.models import Usuario
from api.serializers import MENSAGEM_LOGIN_INVALIDO


class StatusApiTests(APITestCase):
    def test_status_retorna_ok(self):
        resposta = self.client.get(reverse("status-api"))

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.json(), {"status": "ok"})


class LoginTests(APITestCase):
    SENHA = "senha-forte-123"

    def setUp(self):
        self.url = reverse("login")
        self.usuario = Usuario.objects.create_user(
            "gestor@empresa.com", self.SENHA, perfil=Usuario.Perfil.GESTOR
        )

    def test_credenciais_corretas_retornam_token_e_perfil(self):
        resposta = self.client.post(
            self.url, {"email": "gestor@empresa.com", "password": self.SENHA}
        )

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.json()["perfil"], "GESTOR")
        self.assertEqual(resposta.json()["token"], Token.objects.get(user=self.usuario).key)

    def test_token_autentica_requisicoes(self):
        token = self.client.post(self.url, {"email": "gestor@empresa.com", "password": self.SENHA})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.json()['token']}")

        self.assertEqual(self.client.get(reverse("status-api")).status_code, status.HTTP_200_OK)

    def test_senha_errada_nega_acesso_com_mensagem(self):
        resposta = self.client.post(self.url, {"email": "gestor@empresa.com", "password": "errada"})

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resposta.json()["non_field_errors"], [MENSAGEM_LOGIN_INVALIDO])
        self.assertNotIn("token", resposta.json())

    def test_usuario_inativo_com_credenciais_corretas_e_negado(self):
        self.usuario.is_active = False
        self.usuario.save()

        resposta = self.client.post(
            self.url, {"email": "gestor@empresa.com", "password": self.SENHA}
        )

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", resposta.json())
        self.assertFalse(Token.objects.exists())

    def test_campos_obrigatorios(self):
        resposta = self.client.post(self.url, {})

        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(set(resposta.json()), {"email", "password"})

    def test_email_em_caixa_mista_e_o_mesmo_login(self):
        Usuario.objects.create_user("Gestor2@Empresa.com", self.SENHA, perfil=Usuario.Perfil.GESTOR)

        self.assertEqual(Usuario.objects.filter(email="gestor2@empresa.com").count(), 1)
        for email in ("gestor2@empresa.com", "GESTOR2@EMPRESA.COM", " Gestor2@Empresa.com "):
            resposta = self.client.post(self.url, {"email": email, "password": self.SENHA})
            self.assertEqual(resposta.status_code, status.HTTP_200_OK, email)
