# 🗨️ Hashzap - Live Chat Profissional

> Um sistema de chat em tempo real moderno e multiplataforma, desenvolvido com Python. O Hashzap permite a comunicação instantânea tanto via web (Flask + SocketIO) quanto via desktop (Flet), unindo praticidade e uma interface elegante inspirada nos principais apps de mensagens.

![Tela do sistema](https://github.com/vitoriapguimaraes/hashzap/blob/main/demo/navigation.gif)

## Funcionalidades Principais

- **Comunicação em Tempo Real**: Mensagens instantâneas via WebSockets (SocketIO) e PubSub (Flet).
- **Multiplataforma**: Acesse via navegador ou através de um aplicativo desktop nativo.
- **Interface Moderna**: Design limpo com foco em UX, incluindo suporte a gradientes e layouts responsivos.
- **Alinhamento Inteligente**: Mensagens enviadas são alinhadas à direita (estilo WhatsApp) para melhor legibilidade.
- **Sistema de Notificações**: Alertas visuais de entrada e saída de usuários no chat.
- **Segurança e Log**: Gerenciamento de segredos via variáveis de ambiente (.env) e rastreamento completo via logs profissionais.

## Tecnologias Utilizadas

- **Backend**: Python 3.10+ / Flask / Flask-SocketIO
- **UI Desktop**: Flet (Flutter workflow for Python)
- **Frontend Web**: HTML5 / Vanilla CSS / JavaScript (jQuery)
- **Infra**: python-dotenv / Eventlet / Logging

## Como Executar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/vitoriapguimaraes/Python-SiteChatAoVivo.git
   ```

2. **Crie e ative seu ambiente virtual**:

   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor Web**:

   ```bash
   python src/hashzap/flask_app/app.py
   ```

   _Acesse em [http://localhost:5000](http://localhost:5000)_

5. **Inicie o aplicativo Desktop**:

   ```bash
   python src/hashzap/flet_app/main.py
   ```

## Como Usar

1. **Tela Inicial**: Digite seu nome no campo indicado para entrar na conversa.
2. **Chat**: Envie mensagens em tempo real para todos os usuários conectados.
3. **Navegação**: No Desktop, use o botão de "voltar" no topo para sair do chat e retornar à tela inicial.
4. **Alinhamento**: Suas mensagens aparecerão em verde à direita, enquanto as dos outros membros aparecerão à esquerda.

## Estrutura de Diretórios

```bash
/Python-SiteChatAoVivo
├── src/
│   ├── hashzap/
│   │   ├── flask_app/    # Servidor e cliente Web
│   │   ├── flet_app/     # Aplicativo Desktop
│   │   └── config.py     # Configurações globais
├── .env.example          # Modelo de variáveis de ambiente
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação principal
```

## Status

✅ Concluído

> Veja as [issues abertas](https://github.com/hashzap/issues) para sugestões de melhorias e próximos passos.

---

## Mais Sobre Mim

Acesse os arquivos disponíveis na [Pasta Documentos](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
