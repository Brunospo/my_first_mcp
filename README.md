# 🔐 mcp-do-zero

**PT:** Meu primeiro MCP Server — feito do zero, com criptografia.
**EN:** My first MCP Server — built from scratch, with cryptography.

---

## 📖 Visão Geral / Overview

**PT:** Este projeto é um **MCP (Model Context Protocol) Server** que oferece ferramentas de criptografia e descriptografia de mensagens. Ele foi criado como um projeto de aprendizado para entender como o protocolo MCP funciona na prática — conectando LLMs a ferramentas externas de forma padronizada.

**EN:** This project is an **MCP (Model Context Protocol) Server** that provides message encryption and decryption tools. It was created as a learning project to understand how the MCP protocol works in practice — connecting LLMs to external tools in a standardized way.

---

## 🤔 O que é um MCP? / What is an MCP?

**PT:** O **Model Context Protocol** é um protocolo aberto que padroniza como aplicações fornecem contexto a LLMs. Em vez de integrar cada ferramenta manualmente com cada modelo, você cria um **MCP Server** que expõe ferramentas, recursos e prompts de forma padrão. Qualquer cliente compatível com MCP (como Claude, OpenCode, Cursor) pode descobrir e usar essas ferramentas automaticamente.

**EN:** The **Model Context Protocol** is an open protocol that standardizes how applications provide context to LLMs. Instead of manually integrating each tool with each model, you create an **MCP Server** that exposes tools, resources, and prompts in a standard way. Any MCP-compatible client (like Claude, OpenCode, Cursor) can automatically discover and use those tools.

---

## ✨ Funcionalidades / Features

### Ferramentas / Tools

| Ferramenta / Tool | Descrição / Description |
|---|---|
| `encrypt_message` | Criptografa uma mensagem usando Fernet (AES-128-CBC) / Encrypts a message using Fernet (AES-128-CBC) |
| `decrypt_message` | Descriptografa um token Fernet de volta ao texto original / Decrypts a Fernet token back to the original text |

### Recursos / Resources

| Recurso / Resource | Descrição / Description |
|---|---|
| `encryption://info` | Informações sobre o algoritmo de criptografia / Encryption algorithm information |
| `decryption://info` | Informações sobre o processo de descriptografia / Decryption process information |

### Prompts / Prompts

| Prompt | Descrição / Description |
|---|---|
| `encrypt_message_prompt` | Template de prompt para criptografar mensagens / Prompt template for encrypting messages |

---

## 🔧 Como Funciona a Criptografia / How the Cryptography Works

**PT:** O fluxo de criptografia é o seguinte:

1. O usuário fornece uma **passphrase** (qualquer senha/palavra)
2. O servidor deriva uma chave criptográfica usando **PBKDF2-HMAC-SHA256** (100.000 iterações, salt estático)
3. A chave derivada é usada com **Fernet** (AES-128 em modo CBC + HMAC-SHA256 para autenticação)
4. O resultado é um **token Fernet** (string em URL-safe base64)

**EN:** The encryption flow works as follows:

1. The user provides a **passphrase** (any password/word)
2. The server derives a cryptographic key using **PBKDF2-HMAC-SHA256** (100,000 iterations, static salt)
3. The derived key is used with **Fernet** (AES-128 in CBC mode + HMAC-SHA256 for authentication)
4. The result is a **Fernet token** (URL-safe base64-encoded string)

> **⚠️ Nota / Note:** O salt é estático (`static_salt_16bytes`) por simplicidade didática. Em produção, salts devem ser únicos por usuário e armazenados com segurança.
> The salt is static (`static_salt_16bytes`) for didactic simplicity. In production, salts should be unique per user and stored securely.

---

## 🚀 Instalação / Installation

### Pré-requisitos / Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recomendado / recommended) ou pip

### Passo a passo / Step by step

```bash
# Clone o repositório / Clone the repository
git clone <repo-url>
cd mcp-do-zero

# Com uv / With uv
uv sync

# Ou com pip / Or with pip
pip install -e .
```

---

## ▶️ Como Rodar / How to Run

**PT:** O servidor usa o transporte **stdio**, o que significa que ele se comunica via entrada/saída padrão. Isso é ideal para integração com clientes MCP.

**EN:** The server uses the **stdio** transport, meaning it communicates via standard input/output. This is ideal for MCP client integration.

```bash
python src/mcp_do_zero/main.py
```

**PT:** Você deve ver: `Encrypt MCP Server running on stdio...`
**EN:** You should see: `Encrypt MCP Server running on stdio...`

---

## 🔌 Como Usar no OpenCode / How to Use in OpenCode

**PT:** Para usar este MCP Server no OpenCode, adicione a seguinte configuração ao seu `opencode.json`:

**EN:** To use this MCP Server in OpenCode, add the following configuration to your `opencode.json`:

```json
{
  "mcp": {
    "servers": {
      "servidor-criptografia": {
        "type": "local",
        "command": [".venv/bin/python", "src/mcp_do_zero/main.py"]
      }
    }
  }
}
```

**PT:** Depois de configurar, as ferramentas ficam disponíveis automaticamente nas conversas. Por exemplo:
**EN:** After configuring, the tools are automatically available in conversations. For example:

> *"Criptografa a mensagem 'Olá, mundo!' com a chave 'minha-senha-secreta'"*
> *"Encrypt the message 'Hello, world!' with the key 'my-secret-password'"*

---

## 📁 Estrutura do Projeto / Project Structure

```
mcp-do-zero/
├── src/
│   └── mcp_do_zero/
│       ├── __init__.py
│       ├── main.py          # Ponto de entrada / Entry point
│       ├── meu_mcp.py       # Definição do servidor e ferramentas / Server & tools definition
│       ├── service.py       # Lógica de criptografia / Cryptography logic
│       └── types.py         # Schemas Pydantic / Pydantic schemas
├── tests/
│   └── test_meu_mcp.py      # Testes / Tests
├── pyproject.toml           # Configuração do projeto / Project configuration
├── opencode.json            # Configuração MCP do OpenCode / OpenCode MCP config
└── README.md                # Este arquivo / This file
```

---

## 🧪 Testes / Tests

**PT:** Os testes estão em `src/tests/` e usam pytest. Para rodar:

**EN:** Tests are in `src/tests/` and use pytest. To run:

```bash
pytest
```

---

## 📝 Lições Aprendidas / Lessons Learned

**PT:** Criar este MCP do zero foi uma experiência incrível. Algumas coisas que aprendi:

- O protocolo MCP é mais simples do que parece — decoradores `@server.tool()` fazem a mágica acontecer
- O transporte stdio é o mais comum para servidores locais
- A biblioteca `cryptography` do Python é poderosa e bem documentada
- Testar servidores MCP exige um pouco de criatividade (não há HTTP para testar)

**EN:** Building this MCP from scratch was an amazing experience. Some things I learned:

- The MCP protocol is simpler than it looks — `@server.tool()` decorators do the magic
- The stdio transport is the most common for local servers
- Python's `cryptography` library is powerful and well-documented
- Testing MCP servers requires some creativity (no HTTP to test against)

---

## 🔮 Próximos Passos / Next Steps

**PT:** Ideias para evoluir este projeto:

- [ ] Adicionar salt dinâmico por usuário
- [ ] Suporte a diferentes algoritmos de criptografia
- [ ] Mais ferramentas (hash, assinatura digital, etc.)
- [ ] Publicar como pacote pip

**EN:** Ideas to evolve this project:

- [ ] Add dynamic salt per user
- [ ] Support different encryption algorithms
- [ ] More tools (hash, digital signature, etc.)
- [ ] Publish as a pip package

---

## 📄 Licença / License

**PT:** Este projeto é apenas para fins educacionais.
**EN:** This project is for educational purposes only.
