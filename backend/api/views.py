"""Views da API."""

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers import LoginSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def status_api(request: Request) -> Response:
    """Retorna se a API está no ar. Útil para testar a configuração inicial."""
    return Response({"status": "ok"})


@api_view(["POST"])
@authentication_classes([])  # token inválido/inativo no header não pode barrar o login
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    """RF-001: autentica com e-mail e senha e devolve o token e o perfil."""
    serializer = LoginSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    usuario = serializer.validated_data["usuario"]
    token, _ = Token.objects.get_or_create(user=usuario)
    return Response({"token": token.key, "perfil": usuario.perfil})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request: Request) -> Response:
    """RF-002: encerra a sessão apagando o token; novo acesso exige login."""
    request.auth.delete()
    return Response(status=204)
