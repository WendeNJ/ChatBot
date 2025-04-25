from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot


@bot.message_handler(commands=["3"])
def opcao3(mensagem):
    texto = """
    🏆 **Últimos Resultados da FURIA** – Escolha a modalidade:

    🔫 /Cs2Resultados – Counter-Strike 2  
    🎯 /ValorantResultados – Valorant  
    ⚽ /KingsResultados – Kings League  

    /Menu 📜 Voltar ao menu principal
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Cs2Resultados"])
def cs2_resultados(mensagem):
    resultados_cs2 = """
    🔫 **Últimos Resultados da FURIA – CS2**:

    📅 09/04/2025 – ❌ 0x2 vs The MongolZ  
    🏆 PGL Bucharest 2025 – 12º-14º lugar – 💰 $9.375

    📅 22/03/2025 – ❌ 1x2 vs M80  
    🏆 BLAST Open Spring 2025 – 13º-16º lugar – 💰 $5.000

    📅 10/03/2025 – ❌ 1x2 vs Team Falcons  
    🏆 ESL Pro League S21 – 12º-14º lugar – 💰 $10.500

    📅 03/02/2025 – ❌ 1x2 vs Astralis  
    🏆 IEM Katowice 2025 – 13º-16º lugar – 💰 $10.000

    📅 19/01/2025 – ❌ 1x2 vs BetBoom Team  
    🏆 BLAST Bounty Spring 2025: Qualifier – 9º-16º lugar

    /Menu 📜 Voltar ao menu principal
    """
    bot.send_message(mensagem.chat.id, resultados_cs2)

@bot.message_handler(commands=["ValorantResultados"])
def valorant_resultados(mensagem):
    valorant_resultados = """
    📊 **Últimos Resultados da FURIA - Valorant** 🎯

    🗓️ 21/04/2025  
    🏆 VCT 2025: Americas Stage 1  
    📌 11º - 12º lugar  
    📈 0 vitórias em 5 jogos (Fase de Grupos)

    🗓️ 23/01/2025  
    🏆 VCT 2025: Americas Kickoff  
    📌 9º - 12º lugar  
    ❌ Derrota por 0x2 contra Evil Geniuses

    🗓️ 15/12/2024  
    🏆 Tixinha Invitational (B-Tier)  
    🥇 1º Lugar  
    ✅ Vitória por 2x1 contra MIBR  
    💰 Premiação: $6.000

    🗓️ 14/07/2024  
    🏆 VCT 2024: Americas Stage 2  
    📌 10º lugar  
    📈 3 vitórias em 7 jogos (Fase de Grupos)

    🗓️ 05/05/2024  
    🏆 VCT 2024: Americas Stage 1  
    📌 9º - 10º lugar  
    📈 0 vitórias em 5 jogos (Fase de Grupos)

    /Menu 📜 Voltar ao menu principal
    """
    bot.send_message(mensagem.chat.id, valorant_resultados)


@bot.message_handler(commands=["KingsResultados"])
def kings_resultados(mensagem):
    resultados_kings = """
⚽ **Últimos Resultados da FURIA – Kings League Brasil 2025**:

📅 29/03/2025 – ✅ FURIA 6 x 2 Dendele FC  
📅 31/03/2025 – ✅ FURIA 4 x 2 Real Elite  
📅 07/04/2025 – ✅ FURIA 5 x 0 Nyvelados FC  
📅 14/04/2025 – ✅ FURIA 6 x 1 LOUD SC  
📅 21/04/2025 – ✅ FURIA 9 x 7 G3X FC

/Menu 📜 Voltar ao menu principal
"""
    bot.send_message(mensagem.chat.id, resultados_kings)
