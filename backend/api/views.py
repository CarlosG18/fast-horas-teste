"""
Views da API.

Para CRUDs, prefira ViewSets registrados no router de `api/urls.py`:

    class ProdutoViewSet(viewsets.ModelViewSet):
        queryset = Produto.objects.all()
        serializer_class = ProdutoSerializer
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def status_api(request: Request) -> Response:
    """Retorna se a API está no ar. Útil para testar a configuração inicial."""
    return Response({"status": "ok"})
