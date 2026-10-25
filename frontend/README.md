# Nome do Projeto - Front-End
> Descrição do projeto

![React](https://img.shields.io/badge/React-23272f?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-3178c6?logo=typescript&logoColor=white)

# Links importantes 
- [Mockup]()
- [Pipefy]()
- [Repositório do Back]()

## 📋 Sobre o Projeto

Descrição do projeto

## 🚀 Tecnologias Utilizadas

### Core

- **React [versão]** - Biblioteca de JavaScript 
- **TypeScript [versão]** - Superset tipado do JavaScript
- **CSS3** - Linguagem de estilos em cascata
- **Vite [versão]** - Ferramenta de build e servidor local

### Utilitários

- **Node.js** - Ambiente de execução e gerenciador de pacotes
- **ESLint** + **typescript-eslint** - Análise estática do código
- **Prettier** - Formatador de código
- **SCSS [opcional]**- Linguagem de extensão do CSS

## 📁 Estrutura do Projeto

```
Nome do Projeto/
├── public/                    # Arquivos estáticos servidos na raiz (favicon, etc.)
├── src/
│   ├── assets/                # Arquivos de mídia (ícones, imagens, etc.)
│   ├── components/            # Componentes reutilizáveis (.tsx)
│   ├── hooks/                 # Hooks customizados (useAlgo.ts)
│   ├── pages/                 # Telas da aplicação
│   ├── services/              # Comunicação com a API (api.ts)
│   ├── App.tsx                # Componente raiz
│   ├── index.css              # Estilos globais
│   ├── main.tsx               # Ponto de entrada
│   └── vite-env.d.ts          # Tipagem das variáveis de ambiente
├── .vscode/extensions.json    # Extensões recomendadas
├── .editorconfig              # Padrão de indentação/quebra de linha
├── .env.example               # Modelo das variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── .prettierrc                # Configuração do Prettier
├── eslint.config.js           # Configuração do ESLint
├── index.html                 # HTML base
├── package.json               # Dependências e scripts do projeto
├── tsconfig.json              # Configuração do TypeScript (referências)
├── tsconfig.app.json          # Configuração do TS da aplicação (src/)
├── tsconfig.node.json         # Configuração do TS para o vite.config.ts
└── vite.config.ts             # Configuração do Vite
```

## ⚙️ Configuração e Instalação

### Pré-requisitos

- [Node.js](https://nodejs.org/en/download)

### 1. Clone o Repositório

```bash
git clone [link]
cd [nome do projeto]
```

### 2. Variáveis de ambiente e dependências

```bash
cp .env.example .env   # ajuste a VITE_API_URL
npm install
```
### 3. Execução do servidor

```bash
npm run dev
```

O servidor estará disponível em `http://localhost:5173/`

### Outros scripts

```bash
npm run build       # checa os tipos e gera a pasta dist/
npm run preview     # serve o build localmente
npm run typecheck   # só checagem de tipos
npm run lint        # ESLint
npm run format      # Prettier
```

### Padrões de Código

- **ESLint** e **Prettier** sem erros antes de abrir PR (`npm run lint && npm run format`)
- **[TSDoc](https://tsdoc.org/)** para documentação do código
- Evite `any`; tipe props e retornos de API

## 👥 Equipe

- [Membro]() - Scrum Master
- [Membro]()- PO
- [Membro]() - Dev Frontend
- [Membro]()- Dev Backend
---
© 2026 **[EJECT](https://www.ejectufrn.com.br/)** <br>
