import threading
import time

from ProgramPrincipal.Inicializacao.AoVivo import get_furia_live_match_id, conectar_websocket
from ProgramPrincipal.Inicializacao.ChatBotFuria import bot
import ProgramPrincipal.Comandos.Elenco
import ProgramPrincipal.Comandos.Campeonatos
import ProgramPrincipal.Comandos.Resultados
import ProgramPrincipal.Comandos.Historia
import ProgramPrincipal.Comandos.Produtos
import ProgramPrincipal.Comandos.RedesSociais
import ProgramPrincipal.Comandos.Wallpaper
import ProgramPrincipal.Comandos.InLive
import ProgramPrincipal.Comandos.IA
import requests
import os



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
/7 Wallpaper Furia
/8 Partidas ao vivo
/9 Pergunte ao Furinha (resposta inteligente) 🤖"""
    bot.reply_to(mensagem, opcoes)


def run_bot():
    try:
        print("Bot iniciado... aguardando mensagens.")
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Erro ocorrido: {e}")
        time.sleep(5)
        run_bot()

def main():
    while True:
        match_id = get_furia_live_match_id()
        if match_id:
            conectar_websocket(match_id)
            break
        else:
            print("🔎 Esperando a FURIA jogar... tentando novamente em 10 minutos...")
            time.sleep(10000)


if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()


    websocket_thread = threading.Thread(target=main)
    websocket_thread.start()
