# 🗨️ Hashzap - Live Chat Refatorado

Este projeto é uma evolução de um chat em tempo real, agora com uma estrutura mais profissional, utilizando **Python**, **Flask (SocketIO)** e **Flet**.

## ✨ O que mudou?

A versão original foi refatorada para seguir boas práticas de mercado:

- **Organização de código**: Agora com estrutura `src/`, separando lógica de frontend e backend.
- **Configuração profissional**: Uso de arquivo `.env` para segurança e `config.py` para centralizar as definições.
- **Logs inteligentes**: Substituímos o básico `print` por Logging, facilitando o rastreamento de erros e conexões.
- **Interface Moderna**: O chat web foi totalmente redesenhado com foco em UX, usando fontes limpas e design inspirado no WhatsApp.

---

## 🚀 Como executar

### 1. Preparar o ambiente

Recomendamos o uso de um ambiente virtual (venv):

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Instalar dependências (Incluindo o pacote hashzap)

O projeto agora é um pacote Python instalável. Use o comando abaixo para instalar as dependências e o próprio projeto em modo editável:

```bash
pip install -e .
```

### 3. Configurar variáveis de ambiente

Copie o arquivo de exemplo e ajuste se necessário:

```bash
cp .env.example .env
```

### 4. Rodar o Chat

Como o projeto agora é um pacote, você pode rodar os módulos diretamente:

#### 🌐 Versão Web (Flask + SocketIO)

```bash
python src/hashzap/flask_app/app.py
```

Acesse em: `http://localhost:5000`

#### 📱 Versão Desktop (Flet)

```bash
python src/hashzap/flet_app/main.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask / Flask-SocketIO
- **Frontend Web**: HTML5 / CSS3 (Inter Font) / jQuery
- **App UI**: Flet (Flutter workflow for Python)
- **Utilities**: Python-Dotenv / Logging

---

Desenvolvido por github.com/vitoriapguimaraes
