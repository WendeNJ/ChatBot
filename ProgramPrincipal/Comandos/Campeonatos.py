from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot

@bot.message_handler(commands=["2"])
def opcao2(mensagem):
    texto = """
    📅 Próximos Campeonatos da FURIA:

    /Cs2Camps 🔫 Counter-Strike 2  
    /ValorantCamps 🎯 Valorant  
    /KingsCamps ⚽ Kings League
    /Menu 📜 Voltar ao menu principal"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Cs2Camps"])
def cs_campeonatos(mensagem):
    campeoanato_cs2 = """📅 Próximos Campeonatos de CS2 da FURIA:

🎯 PGL Astana 2025
🗓️ 10 a 18 de maio
🌍 Astana, Cazaquistão
🔥 Preparando a mira pro alto nível!

🎯 IEM Dallas 2025
🗓️ 19 a 25 de maio
🌍 Dallas, EUA
💥 Vai ter FURIA nos States!

🎯 BLAST.tv Austin Major 2025
🗓️ 02 a 22 de junho
🌍 Austin, EUA
🏆 Rumo ao Major, FURIOSOS!

/Menu 📜 Voltar ao menu principal"""
    bot.send_message(mensagem.chat.id, campeoanato_cs2)

@bot.message_handler(commands=["ValorantCamps"])
def valorant_campeonatos(mensagem):
    campeonato_vava = """
🎯 Próximos Campeonatos de Valorant:

🏆 **VCT 2025: Americas Stage 2**  
📅 01 de Julho a 01 de Agosto

/Menu 📜 Voltar ao menu principal
"""
    bot.send_message(mensagem.chat.id, campeonato_vava)



@bot.message_handler(commands=["KingsCamps"])
def campeonatos_kings(mensagem):
        campeonato_kings = """
    ⚽ A FURIA atualmente está participando da **Kings League Brasil 2025**.

    /Menu 📜 Voltar ao menu principal
    """
        bot.send_message(mensagem.chat.id, campeonato_kings)
