# Nome do Projeto - Back-End
> Descrição breve do projeto.

![Django](https://img.shields.io/badge/Django-6.0.8-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.18.1-A30000?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)

# Links importantes
- [Mockup]()
- [Pipefy]()
- [Repositório do Front]()

## 📋 Sobre o Projeto

Descrição do projeto.

## 🚀 Tecnologias Utilizadas

### Core

- **Django 6.0.8** - Framework web principal
- **Django Rest Framework 3.18.1** - Framework para construção de API REST

### Utilitários

- **django-cors-headers** - Libera o acesso da API para o front-end (CORS)
- **python-decouple** - Leitura das variáveis de ambiente do arquivo `.env`
- **WhiteNoise** e **Gunicorn** - Arquivos estáticos e servidor de produção
- **Ruff** - Linter e formatador para código Python

## 📁 Estrutura do Projeto

```
Nome do Projeto/
├── api/                       # App da API: models, serializers, views e rotas
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py                # Configuração de endpoints
│   └── views.py
├── setup/                     # Configurações do Django
│   ├── settings.py
│   └── urls.py
├── .env.example               # Modelo das variáveis de ambiente
├── Dockerfile
├── docker-compose.yml
├── ruff.toml                  # Configuração do Ruff
├── requirements.txt           # Dependências Python
├── manage.py                  # Utilitário Django
└── README.md                  # Este arquivo
```

## ⚙️ Configuração e Instalação

### Pré-requisitos

- Python 3.12+

### 1. Clone o Repositório

```bash
git clone [link]
cd [nome do projeto]
```

### 2. Configuração do Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalação das Dependências

```bash
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente

Copie o arquivo de exemplo e ajuste os valores se necessário:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

### 5. Migrações do Banco

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criação do Superusuário

```bash
python manage.py createsuperuser
```

### 7. Execução do Servidor

```bash
python manage.py runserver
```

O servidor estará disponível em `http://localhost:8000`.

Para conferir se está tudo certo, acesse `http://localhost:8000/api/status/` — a resposta deve ser `{"status": "ok"}`.

| Rota        | Descrição                             |
|-------------|---------------------------------------|
| `/api/`     | Raiz da API (navegável pelo DRF)      |
| `/admin/`   | Painel administrativo do Django       |
| `/api-auth/`| Login/logout da API navegável         |

### 8. Testes

```bash
python manage.py test
```

### Docker

Antes de subir com Docker, crie o arquivo `.env` (passo 4).

```bash
# Build da imagem padrão
docker build -t modelo-template .

# Executar com docker-compose
docker compose up -d

# Criar superusuário dentro do container
docker compose exec web python manage.py createsuperuser
```

### Variáveis de Ambiente para Produção

```bash
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com
SECRET_KEY=chave-super-secreta-para-producao
CSRF_TRUSTED_ORIGINS=https://seu-dominio.com
CORS_ALLOWED_ORIGINS=https://endereco-do-front.com
```

Para gerar uma `SECRET_KEY` nova:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Padrões de Código

- **PEP 8** para formatação Python
- **Docstrings** para funções e classes
- **Português** para nomes de domínio (models, campos, serializers, views), mantendo em inglês o que é sintaxe do framework (`Meta`, `ForeignKey`, `Serializer`...)

## Utilizando o ruff

O [ruff](https://docs.astral.sh/ruff/) é uma ferramenta poderosa para fazer linting e
formatação do código. As regras do projeto estão em `ruff.toml`. Abaixo está descrita a sua utilização básica:

### Linter

Para fazer o linting do código utilize:
```
ruff check
```

Para aplicar as correções apontadas pelo linter utilize:
```
ruff check --fix
```

### Formatador

Para formatar o código utilize:
```
ruff format
```

## 👥 Equipe

- Membro - Scrum Master
- Membro - PO
- Membro - Dev Frontend
- Membro - Dev Backend

Desenvolvido pela **EJECT - Empresa Júnior da Escola de Ciências e Tecnologia**
