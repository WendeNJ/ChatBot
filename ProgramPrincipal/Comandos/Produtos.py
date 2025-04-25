from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot

@bot.message_handler(commands=["5"])
def produtos_oficiais(mensagem):
    produtos_furia = """
🛍️ **Produtos oficiais da FURIA** 🛍️

Se você está procurando produtos oficiais da FURIA, como camisas, bonés, e outros itens, acesse o nosso site oficial: 

👉 [FURIA.gg - Produtos Oficiais](https://furia.gg)

Explore nossa loja e garanta seu item favorito para torcer pela nossa equipe com estilo!

E não se esqueça de mostrar o seu amor pela FURIA nas redes sociais! 💥 Use a hashtag #SOUFURIA e compartilhe sua paixão com a gente! 🔥

/Menu 📜 Voltar ao menu principal
    """
    bot.reply_to(mensagem, produtos_furia)
