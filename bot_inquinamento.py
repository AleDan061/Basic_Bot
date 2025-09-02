import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l/ accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def somma(ctx, a = 5):
    await ctx.send(a+ 5)

@bot.command()
async def leggi(ctx):
    with open('C:/Users/andre/VScode.projects/Bot/text.txt', 'r', encoding='utf-8') as f:
        #print(f.read())
        await ctx.send(f.read())

@bot.command()
async def scrivi(ctx):
    with open('C:/Users/andre/VScode.projects/Bot/text.txt', 'w', encoding='utf-8') as f:
        testo = 'Ciao di nuovo'
        f.write(testo)

@bot.command()
async def meme_1(ctx):
    with open('C:/Users/andre/VScode.projects/Bot/images/meme1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def random_meme(ctx):
    img_name = random.choice(os.listdir('C:/Users/andre/VScode.projects/Bot/images'))
    with open(f'C:/Users/andre/VScode.projects/Bot/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)    

@bot.command()
async def somma_param(ctx, numero : int):
    await ctx.send(numero + 7)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def inquinamento(ctx):
    with open('C:/Users/andre/Bot_Inquinamento/definizione_inquinamento.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
@bot.command()
async def idee_inquinamento(ctx):
    idee = ['l/inquinamento danneggia l/ambiente',
        'Le auto producono inquinamento',
        'Il consumo di carne rossa crea inquinamento']
    for i in range(3):
        idea = random.choice(idee)
    await ctx.send(idea)

bot.run('TOKEN')
