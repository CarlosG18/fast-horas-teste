"""Serializers da API."""

from django.contrib.auth import authenticate
from rest_framework import serializers

MENSAGEM_LOGIN_INVALIDO = "E-mail ou senha incorretos."


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        # authenticate() devolve None para senha errada e para usuário inativo (RF-003),
        # com a mesma mensagem, para não revelar se o e-mail existe.
        usuario = authenticate(
            request=self.context.get("request"), email=attrs["email"], password=attrs["password"]
        )
        if usuario is None:
            raise serializers.ValidationError(MENSAGEM_LOGIN_INVALIDO)
        attrs["usuario"] = usuario
        return attrs
