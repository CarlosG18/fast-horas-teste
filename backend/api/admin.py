"""
Registro dos models no Django Admin.

Exemplo:

    @admin.register(Produto)
    class ProdutoAdmin(admin.ModelAdmin):
        list_display = ["nome", "preco", "criado_em"]
        search_fields = ["nome"]
"""

from django.contrib import admin  # noqa: F401
