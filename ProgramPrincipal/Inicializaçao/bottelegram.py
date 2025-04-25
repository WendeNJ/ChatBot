import time
from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot
import ProgramPrincipal.Comandos.Elenco
import ProgramPrincipal.Comandos.Campeonatos
import ProgramPrincipal.Comandos.Resultados
import ProgramPrincipal.Comandos.Historia
import ProgramPrincipal.Comandos.Produtos
import ProgramPrincipal.Comandos.RedesSociais
import ProgramPrincipal.Comandos.Wallpaper

@bot.message_handler(commands=["7"])
def opcao7(mensagem):
    pass


def Menu(mensagem):
    return True


@bot.message_handler(func=Menu)
def responder(mensagem):
    opcoes = """
    ⚡ FALA, FURIOSO! ⚡

Sou o **Furinha** 🐆, o bot oficial da FURIA, e tô aqui pra te ajudar no que precisar! Escolhe uma das opções abaixo:

/1 Elenco atual da FURIA 🧑‍🤝‍🧑  
/2 Próximos campeonatos 📅  
/3 Últimos resultados 🏆  
/4 História da FURIA 📖  
/5 Produtos oficiais 🛍️  
/6 Redes sociais 🌐  
/7 Wallpaper Furia"""

    bot.reply_to(mensagem, opcoes)


def run_bot():
    try:
        print("Bot iniciado... aguardando mensagens.")
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Erro ocorrido: {e}")
        time.sleep(5)
        run_bot()


run_bot()
