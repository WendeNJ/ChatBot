# 🤖 ChatBot FURIA — Telegram + IA

Bot para Telegram desenvolvido em Python com comandos relacionados à FURIA e integração com IA generativa.

O projeto reúne funcionalidades de consulta, conteúdo e interação em módulos separados, além de integração com serviços externos.

## ✨ Funcionalidades

- Integração com **Telegram Bot API**
- Comando com **Gemini** para respostas em linguagem natural
- Consulta de campeonatos, resultados e informações do elenco
- Recursos para partidas ao vivo
- Conteúdos sobre história, produtos, redes sociais e wallpapers
- Organização dos comandos em módulos independentes

## 🧱 Estrutura

```text
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
├── Inicializacao/
├── Procfile
└── requirements.txt
```

## 🛠️ Tecnologias

`Python` `pyTelegramBotAPI` `Gemini` `Requests` `python-dotenv`

## ▶️ Como executar

```bash
git clone https://github.com/WendeNJ/ChatBot.git
cd ChatBot/ProgramPrincipal
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente utilizadas pelo bot e pelas integrações antes de iniciar a aplicação.

> Nunca envie tokens, chaves de API ou arquivos `.env` para o repositório.

## 🎯 O que este projeto demonstra

- Integração com APIs externas
- Desenvolvimento de bots
- Organização modular de funcionalidades
- Tratamento de comandos e respostas
- Uso de IA generativa em uma aplicação real

## 👨‍💻 Autor

**Wenderson Carvalho de Araújo Mota**

[LinkedIn](https://www.linkedin.com/in/wendersonmota/) · [GitHub](https://github.com/WendeNJ)
