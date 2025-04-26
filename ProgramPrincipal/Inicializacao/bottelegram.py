import time
from ProgramPrincipal.Inicializacao.ChatBotFuria import bot
import ProgramPrincipal.Comandos.Elenco
import ProgramPrincipal.Comandos.Campeonatos
import ProgramPrincipal.Comandos.Resultados
import ProgramPrincipal.Comandos.Historia
import ProgramPrincipal.Comandos.Produtos
import ProgramPrincipal.Comandos.RedesSociais
import ProgramPrincipal.Comandos.Wallpaper



def Menu(mensagem):
    return True


@bot.message_handler(func=Menu)
def responder(mensagem):
    opcoes = """
    ⚡ FALA, FURIOSO! ⚡

Olá, eu sou o Furinha 🐆, o assistente oficial da FURIA! Estou aqui para te ajudar com tudo o que você precisar. Selecione uma das opções abaixo e vamos lá! 💥

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
