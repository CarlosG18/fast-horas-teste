"""
Serializers da API.

Exemplo:

    class ProdutoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Produto
            fields = ["id", "nome", "preco", "criado_em"]
            read_only_fields = ["id", "criado_em"]

Regras de validação de negócio ficam aqui (métodos `validate_<campo>` ou
`validate`), e não só no front-end.
"""

from rest_framework import serializers  # noqa: F401
