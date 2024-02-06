import discord
import jojocord
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

users = []

# Cria uma nova instância de usuário
async def comecar_jogo(msg):
    for u in users:
        if u.username == msg.author:
            await msg.channel.send("Você já tem um stand.")
            return

    u = jojocord.User([], msg.author)
    u.get_1st_stand()
    await msg.channel.send("Você acabou de despertar seu stand!\n\n" +
        f"Stand: {u.stands[0].nome}\n\n")

    users.append(u)

# Mostra informações de um jogador
async def mostrar_info_user(msg):
    args = msg.content.split(" ")

    if len(args) == 1:
        for u in users:
            if u.username == msg.author:
                stands = ""
                for s in u.stands:
                    stands += s.to_string()

                await msg.channel.send(stands)
                return

        await msg.channel.send("Você ainda não tem um stand. Use !@j-comecar " +
            "para despertar seu stand!")
        return 

    for u in users:
        if u.username.lower() == args[1].lower():
            stands = ""
            for s in u.stands:
                stands += s.to_string()

            await msg.channel.send(stands)
            return

    await msg.channel.send(f"{args[1]} ainda não tem um stand.")

# Inicia uma batalha entre 2 jogadores
async def comecar_batalha(msg):
    pass

# Mostra todos os comandos do bot
async def mostrar_help(msg):
    await msg.channel.send("**Comandos:**\n\n" +
        "**!@j-comecar**: Desperta seu primeiro stand;\n" +
        "**!@j-info**: Mostra seus stands;\n" +
        "**!@j-info <username>**: Mostra os stands de um jogador;\n" +
        "**!@j-fight <username>**: Começa uma batalha com outro jogador (em breve!);\n" +
        "**!@j-help**: Mostra esta lista de comandos;\n" +
        "**!@j-trocar <username>**: Começa uma troca de stands com outro jogador (em breve!)")

# Inicia uma troca de stands entre 2 jogadores
async def comecar_troca(msg):
    pass

cmds = {
    "!@j-comecar": comecar_jogo,   # Passa tutorial + Recebe um stand
    "!@j-info": mostrar_info_user, # Dá informações de seus stands
    "!@j-fight": comecar_batalha,  # Inicia uma batalha
    "!@j-help": mostrar_help,      # Lista de comandos
    "!@j-trocar": comecar_troca    # Trocar stands com outro jogador
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith('!@'):
        try:
            await cmds[msg.content.split(" ")[0]](msg)
        except:
            await msg.channel.send("Erro ao executar comando. Verifique se " +
                "você está o usando corretamente e tente novamente.")

print(os.environ)
client.run(os.environ.get("DISCORD_KEY"))
