# ChatBot FURIA

Este é um chatbot desenvolvido para fornecer informações sobre a FURIA Esports, incluindo dados sobre a organização, suas modalidades, resultados, redes sociais e suporte.

## Funcionalidades

- **Informações sobre a FURIA**: História, modalidades, equipes e conquistas da organização.
- **Redes Sociais**: Links para acompanhar a FURIA nas principais redes sociais.
- **Suporte**: Contatos de suporte via e-mail e WhatsApp.
- **Produtos Oficiais**: Acesso à loja oficial da FURIA para adquirir produtos como camisas, bonés e outros itens.
- **Wallpaper**: Envio de wallpapers oficiais da FURIA.
- **Comandos de Interação**: O bot oferece uma interface simples para interação com o usuário, permitindo acesso rápido aos dados da FURIA.

## Tecnologias Utilizadas

- **Python**: Linguagem utilizada para o desenvolvimento do bot.
- **Telebot**: Biblioteca Python usada para a integração com a API do Telegram.
- **GitHub**: Repositório para controle de versão e colaboração.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- `pip` para gerenciar pacotes Python

### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/WendeNJ/ChatBot.git
    cd ChatBot
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    .\venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` para armazenar seu **token** do bot do Telegram e outros dados confidenciais.

### Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto e adicione o seguinte:

