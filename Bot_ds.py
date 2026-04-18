import discord
import random
from discord.ext import commands

colores = ["verde", "rojo", "azul", "amarillo"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
especiales = ["+2", "reverse", "bloqueo"]
comodines = ["cambio de color", "+4"]
mazo = []
manos = {}
for color in colores:
    for numero in numeros:
        mazo.append((color, numero))
    for especial in especiales:
        mazo.append((color, especial))
for comodin in comodines:
   mazo.append((None, comodin))
   

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def iniciarUNO(ctx):
    manos.clear()
    for i in range(7):
        carta = random.choice(mazo)
        manos.append(carta)
        await ctx.send(f"mano: {manos}")

@bot.command()
async def robar(ctx):
    usuario = ctx.author.id
    carta = random.choice(mazo)
    if carta[0] is None:
        await ctx.author.send(f'Has robado la carta: {carta[1]}')
    else:
        await ctx.author.send(f'Has robado la carta: {carta[0]} {carta[1]}')
    manos[usuario].append(carta)

bot.run("")