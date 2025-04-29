from ProgramPrincipal.Inicializacao.ChatBotFuria import bot
from ProgramPrincipal.Inicializacao.GeminiFuria import GeminiFURIA


gemini = GeminiFURIA()

@bot.message_handler(commands=["9"])
def comando_gemini(mensagem):
    pergunta = mensagem.text[3:].strip()

    if not pergunta:
        return bot.send_message(mensagem.chat.id, "🐆 Fala aí! Escreva sua pergunta depois do /9")

    try:
        resposta = gemini.perguntar(pergunta)
        bot.send_message(mensagem.chat.id, f"🐾 {resposta}")
    except Exception as e:
        print(f"Erro: {e}")  # Para debug
        bot.send_message(mensagem.chat.id, "🐆 O servidor tá ocupado! Tenta de novo!")