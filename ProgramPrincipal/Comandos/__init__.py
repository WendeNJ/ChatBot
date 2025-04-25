



from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot


@bot.message_handler(commands=["cs"])
def cs (mensagem):
    textoCs = """
🔫 Elenco atual da FURIA (CS2) – Atualizado manualmente:

🐍 FalleN – Capitão e AWPer lendário  
⚡ YEKINDAR – Rifler explosivo e agressivo  
🎯 yuurih – Consistente e decisivo  
🔥 KSCERATO – Um dos melhores do Brasil  
🧊 molodoy – Reforço promissor na line

Vamos pra cima, FURIOSO! 🐆💜 #DaleFURIA
"""
    bot.send_message(mensagem.chat.id, textoCs)


