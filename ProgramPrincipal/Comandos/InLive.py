import threading

from ProgramPrincipal.Inicializacao.AoVivo import get_furia_live_match_id, conectar_websocket
from ProgramPrincipal.Inicializacao.ChatBotFuria import bot

@bot.message_handler(commands=["8"])
def responder_partidas_ao_vivo(mensagem):

    opcoes = "🔎 Buscando partidas ao vivo da FURIA..."
    bot.reply_to(mensagem, opcoes)


    match_id = get_furia_live_match_id()
    if match_id:
        conectar_websocket(match_id)
        bot.reply_to(mensagem, f"⚡ FURIA está jogando! Acompanhe o placar ao vivo.")
    else:
        bot.reply_to(mensagem, "❌ Não há partidas ao vivo no momento. Tente novamente em breve.")
