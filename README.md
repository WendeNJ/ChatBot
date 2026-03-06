<p align="center">
  <img src="https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
</p>

<h1 align="center">🤖 ChatBot FURIA</h1>

<p align="center">
  Chatbot inteligente no Telegram com integração ao <b>Gemini AI</b>, dados em tempo real da FURIA Esports via <b>PandaScore API</b> e atualizações ao vivo via <b>WebSocket</b>.
</p>

---

## 📌 Sobre o Projeto

Chatbot desenvolvido em Python para fãs da FURIA Esports, trazendo informações atualizadas sobre o time diretamente no Telegram. O diferencial é a integração com **IA generativa (Gemini)** e monitoramento de partidas ao vivo via WebSocket.

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🏆 Informações da FURIA | História, modalidades e conquistas |
| 👥 Elenco atualizado | Times por modalidade |
| 📺 Resultados e Jogos ao Vivo | Partidas em andamento via PandaScore |
| 🔴 WebSocket ao vivo | Eventos em tempo real durante as partidas |
| 🌐 Redes Sociais | Links diretos para as redes da FURIA |
| 🛒 Produtos Oficiais | Link para a loja oficial |
| 🖼️ Wallpapers | Wallpapers oficiais para download |
| 🧠 IA Integrada | Respostas automatizadas com Gemini AI |
| 🧪 Gemini FURIA | Chat inteligente experimental com contexto da FURIA |

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| pyTelegramBotAPI (Telebot) | Integração com Telegram |
| PandaScore API | Dados de partidas e resultados |
| WebSocket | Atualizações em tempo real |
| Gemini AI (Google) | IA generativa para chat inteligente |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Requests | Chamadas HTTP às APIs |

---

## 🏗️ Estrutura do Projeto

```
ProgramPrincipal/
├── Comandos/
│   ├── Campeonatos.py      # Info sobre campeonatos
│   ├── Elenco.py           # Elenco atual da FURIA
│   ├── Historia.py         # História da organização
│   ├── IA.py               # Integração com IA
│   ├── InLive.py           # Partidas ao vivo (WebSocket)
│   ├── Produtos.py         # Loja oficial
│   ├── RedesSociais.py     # Links das redes sociais
│   ├── Resultados.py       # Últimos resultados
│   └── Wallpaper.py        # Wallpapers oficiais
│
├── Inicializacao/
│   ├── AoVivo.py           # Monitor de partidas em andamento
│   ├── bottelagram.py      # Configuração do bot Telegram
│   ├── ChatBotFuria.py     # Ponto de entrada principal
│   └── GeminiFuria.py      # Chat experimental com Gemini
│
├── .env                    # Variáveis de ambiente (não versionar)
└── requirements.txt        # Dependências do projeto
```

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3.8+
- Chaves de API: Telegram Bot, PandaScore e Gemini

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/WendeNJ/ChatBot.git
cd ChatBot

# 2. Crie e ative o ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
```

### Configuração do `.env`

```env
TELEGRAM_TOKEN=seu_token_aqui
PANDASCORE_TOKEN=seu_token_aqui
GEMINI_API_KEY=sua_chave_aqui
```

```bash
# 5. Execute o bot
python ProgramPrincipal/Inicializacao/ChatBotFuria.py
```

---

## 🔴 Integração WebSocket — Partidas ao Vivo

A aplicação monitora automaticamente partidas em andamento da FURIA no CS:GO consultando o endpoint `/matches/running` da PandaScore API. Quando uma partida é detectada, conecta-se ao WebSocket para receber eventos em tempo real, com reconexão automática em caso de falha.

---

## 🗺️ Roadmap

- [x] Comandos básicos de informação
- [x] Integração com PandaScore API
- [x] Monitoramento ao vivo via WebSocket
- [x] IA com Gemini integrado
- [ ] Suporte a mais modalidades além de CS:GO
- [ ] Notificações automáticas de início de partida
- [ ] Dashboard web para administração

---

## 👨‍💻 Autor

**Wenderson Carvalho de Araújo Mota**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-linkedin)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/WendeNJ)
