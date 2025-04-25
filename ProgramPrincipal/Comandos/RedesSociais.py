from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot

@bot.message_handler(commands=["6"])
def redes_sociais(mensagem):
    redes_furia = """
     ⚡ **Redes Sociais da FURIA** ⚡

    Acompanhe tudo sobre a FURIA nas redes sociais e fique por dentro de novidades, resultados e muito mais! Conecte-se com a nossa comunidade e mostre sua paixão pela nossa equipe.

    ⚡ Instagram: [@furia](https://www.instagram.com/furia/)  
    
    ⚡ Twitter (X): [@FURIA](https://twitter.com/FURIA)  
    
    ⚡ Facebook: [@FURIA](https://www.facebook.com/FURIA)  
    
    ⚡ YouTube: [FURIA](https://www.youtube.com/c/FURIA)  
    
    ⚡ Twitch: [FURIA](https://www.twitch.tv/furia)

    Siga-nos, compartilhe e não perca nenhum momento da nossa jornada!

    /Menu 📜 Voltar ao menu principal
    """
    bot.reply_to(mensagem, redes_furia)
