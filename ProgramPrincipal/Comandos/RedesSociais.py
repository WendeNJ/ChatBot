from ProgramPrincipal.Inicializacao.ChatBotFuria import bot

@bot.message_handler(commands=["6"])
def redes_sociais(mensagem):
    redes_furia = """
     ⚡ **Redes Sociais da FURIA** ⚡

    Acompanhe tudo sobre a FURIA nas redes sociais e fique por dentro de novidades, resultados e muito mais! Conecte-se com a nossa comunidade e mostre sua paixão pela nossa equipe.

    ⚡ Instagram: (www.instagram.com/furiagg)  
    
    ⚡ Twitter (X): (x.com/FURIA)  
    
    ⚡ Facebook: (//www.facebook.com/furiagg)  
    

    Siga-nos, compartilhe e não perca nenhum momento da nossa jornada!

    /Menu 📜 Voltar ao menu principal
    """
    bot.reply_to(mensagem, redes_furia)
