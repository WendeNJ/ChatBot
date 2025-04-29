# 🤖 ChatBot FURIA

Um chatbot informativo desenvolvido com Python para fornecer **dados atualizados e relevantes sobre a FURIA Esports**, como resultados, elenco, produtos oficiais e muito mais!

---

## 📌 Funcionalidades

- 🏆 **Informações sobre a FURIA**
  - História, modalidades e conquistas da organização.
  - Elenco atualizado por modalidade.

- 📺 **Resultados e Jogos Ao Vivo**
  - Últimos resultados em torneios.
  - Status de partidas em andamento.

- 🌐 **Redes Sociais**
  - Links para Instagram, Twitter, Facebook, Instagram.

- 🛒 **Produtos Oficiais**
  - Link direto para a loja oficial da FURIA.

- 🖼️ **Wallpapers**
  - Wallpapers oficiais para download.

- 💬 **Comandos interativos**
  - Interface amigável via Telegram com comandos simples.

- 🧠 **IA Integrada**
  - Respostas automatizadas com base em inteligência artificial.

- 🧪 **Gemini FURIA (Experimental)**
  - Chat inteligente com integração ao modelo Gemini.

Toda a lógica está automatizada para reconectar em caso de falha e exibir o ID da partida e os eventos recebidos.
---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Telebot (pyTelegramBotAPI)**
- **python-dotenv**
- **Requests**
- **GitHub (controle de versão)**

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/WendeNJ/ChatBot.git
cd ChatBot

ProgramPrincipal/
├── Comandos/
│   ├── Campeonatos.py
│   ├── Elenco.py
│   ├── Historia.py
│   ├── IA.py
│   ├── InLive.py
│   ├── Produtos.py
│   ├── RedesSociais.py
│   ├── Resultados.py
│   └── Wallpaper.py
│
├── Inicializacao/
│   ├── AoVivo.py
│   ├── bottelagram.py
│   ├── ChatBotFuria.py
│   └── GeminiFuria.py
│
├── .env

4. Configure seu arquivo .env na raiz do projeto
TELEGRAM_TOKEN= ( API_REFERENTE)
PANDASCORE_TOKEN=  (API_REFERENTE)
GEMINI_API_KEY= (API_REFERENTE)

✅ Status do Projeto
🚧 Em desenvolvimento contínuo

🧪 Testes em novas funcionalidades com IA

🙌 Contribuições e feedbacks são bem-vindos!

---

🔴 Atualização em tempo real dos jogos da FURIA (CS:GO)
Implementei a integração com a API do PandaScore para detectar e acompanhar partidas ao vivo da FURIA no CS:GO.

A aplicação consulta automaticamente partidas em andamento (/matches/running) e identifica se a FURIA está jogando.

Se uma partida for encontrada, a aplicação se conecta a um WebSocket do PandaScore, que fornece atualizações em tempo real da partida.
