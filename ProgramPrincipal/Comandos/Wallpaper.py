from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot


@bot.message_handler(commands=["7"])
def opcao7(mensagem):
    wallpapers_furia = """
    🖼️ **Wallpapers Oficiais da FURIA** 🖼️

    Aqui você encontra alguns wallpapers incríveis para deixar o seu dispositivo ainda mais estiloso e com a cara da FURIA! 

    Escolha seu wallpaper favorito e compartilhe com a nossa comunidade!

    📥 **Baixe os wallpapers:**

    - [Clique aqui para Wallpaper 1](https://pbs.twimg.com/media/F98rmOiWYAAFMyD?format=jpg&name=large)
    - [Clique aqui para Wallpaper 2](https://pbs.twimg.com/media/F98rnl8XwAAnrpY?format=jpg&name=large)
  

    📲 **Curta e compartilhe com seus amigos!** Não se esqueça de usar a hashtag #SOUFURIA para mostrar como você apoia a nossa equipe!

    /Menu 📜 Voltar ao menu principal
    """
    bot.reply_to(mensagem, wallpapers_furia, parse_mode='Markdown')
