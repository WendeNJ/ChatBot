from ProgramPrincipal.Inicializaçao.ChatBotFuria import bot

@bot.message_handler(commands=["4"])
def historia_furia(mensagem):
    historia_furia = """

📖 História da FURIA Esports 🐆

A FURIA foi fundada em 2017 por André Akkari, Jaime Pádua e Cris Guedes. Desde o seu início, a organização se destacou no cenário de Counter-Strike: Global Offensive (CS:GO) e, ao longo dos anos, conquistou uma enorme base de fãs e reconhecimento mundial. 🌍

### 🏁 O Início da Jornada (2017):
A FURIA nasceu com o objetivo de representar o Brasil nas competições internacionais de esports. O time de CS:GO foi o primeiro grande destaque, alcançando grandes resultados logo no início e se tornando uma das equipes mais respeitadas do país. 🇧🇷

### 🚀 Expansão para Novas Modalidades:
Com o sucesso no CS:GO, a FURIA começou a expandir suas operações para outras modalidades, incluindo:

- Counter-Strike 2 💣  
- Rocket League 🚗  
- League of Legends ⚔️  
- Valorant 🎯  
- Rainbow Six: Siege 💥  
- Apex Legends 🏹  
- Kings League ⚽  

Essa expansão demonstrou a capacidade da organização em se adaptar e buscar sempre a excelência em novas áreas. Além disso, a FURIA se tornou uma referência em inovação e presença nas mais diversas modalidades de esports. 🎮

### 🏆 Principais Títulos e Conquistas:
A FURIA tem uma lista impressionante de títulos e conquistas em várias modalidades, consolidando sua posição como uma das maiores organizações de esports do Brasil e do mundo. Entre os maiores feitos, destacam-se:

- CS:GO: A FURIA se destacou no cenário internacional, com participações marcantes em torneios como IEM Katowice, ESL Pro League, e o VCT.  

- Valorant: A FURIA se tornou uma das equipes mais fortes no Valorant, com grandes performances em campeonatos internacionais.  

- Rainbow Six Siege: Também marcou sua presença no Rainbow Six, com títulos importantes no cenário competitivo brasileiro.

A organização também alcançou grandes posições em torneios de Rocket League, League of Legends e Apex Legends, com o time de Kings League brilhando no futebol de 7.

### 🌍 Presença Global:
Com escritórios em diferentes países, como Estados Unidos 🇺🇸, Malta 🇲🇹 e China 🇨🇳, a FURIA tem expandido sua presença global, tornando-se uma potência no cenário internacional.

### 👥 A Base de Fãs:
A FURIA é amplamente reconhecida por sua base de fãs apaixonada, que acompanha de perto cada conquista e cada jogo. A organização também se destaca pelas suas atividades nas redes sociais 📱, sempre conectada com seu público e promovendo o engajamento da comunidade.

### 🔥 A Filosofia FURIA:
A FURIA representa dedicação, excelência e paixão pelos esports. Cada jogador, cada título e cada momento dentro da organização reflete o compromisso de sempre ir além e alcançar o topo.

Vamos juntos, FURIOSO! 🐆💜 #DaleFURIA

/Menu 📜 Voltar ao menu principal
"""
    bot.send_message(mensagem.chat.id, historia_furia)
