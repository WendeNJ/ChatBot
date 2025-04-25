from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot





@bot.message_handler(commands=["1"])
def opcao1(mensagem):
    texto = """
    👥 Qual elenco você quer saber, FURIOSO? 🐆

Escolha uma das modalidades:

/Cs2 🔫 Counter-Strike 2  
/Valorant 🎯 Valorant  
/Kings ⚽ Kings League
/Menu 📜 Voltar ao menu principal"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Cs2"])
def Cs(mensagem):
    elenco_cs2 = """
🔫 Elenco atual da FURIA (CS2) –

⚡ FalleN – Capitão e AWPer lendário  
⚡ YEKINDAR – Rifler explosivo e agressivo  
⚡ yuurih – Consistente e decisivo  
⚡ KSCERATO – Um dos melhores do Brasil  
⚡ molodoy – Reforço promissor na line
⚡ sidde – Coach cerebral e estrategista fora do servidor

Vamos pra cima, FURIOSO! 🐆💜 #DaleFURIA

/Menu 📜 Voltar ao menu principal
"""
    bot.send_message(mensagem.chat.id, elenco_cs2)


@bot.message_handler(commands=["Valorant"])
def Valorant(mensagem):
    elenco_valorant = """
  🎯 Elenco atual da FURIA (Valorant) –:

⚡ khalil  
⚡ havoc  
⚡ heat  
⚡ raafa  
⚡ pryze  

    Vamos pra cima, FURIOSO! 🐆💜 #DaleFURIA
    
    /Menu 📜 Voltar ao menu principal """
    bot.send_message(mensagem.chat.id, elenco_valorant)


@bot.message_handler(commands=["Kings"])
def kings(mensagem):
    elenco_kings = """
 🐆 **Elenco da FURIA FC na Kings League Brasil** ⚽

**🎟️ Wildcards:**
- Leleti  
- Lipão  
- Jeffinho

**🧤 Goleiros:**
- Matheus Ayosa  
- Victor Hugo da Silva

**🛡️ Defensor:**
- João Pelegrini

**🎯 Meio-campistas:**
- Caio Carvalho  
- Andrey Wurthmann  
- Matheus de Oliveira

**⚡ Atacantes:**
- Guilherme Monagatti  
- Murilo Donato  
- Ryan Lima  
- Gabriel Pastuch

Vamos com tudo, FURIOSO! 💜🐆 #KingsLeague #FURIAFC

/Menu 📜 Voltar ao menu principal
"""
    bot.send_message(mensagem.chat.id, elenco_kings)
