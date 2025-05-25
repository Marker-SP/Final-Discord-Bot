import discord
from discord.ext import commands
import password as fonk
import game as gm
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logined.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiple(ctx, left: int, right: int):
    """Multiples two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def password(ctx):
    şifre = fonk.parola()
    await ctx.send(şifre)

@bot.command()
async def mathelp(ctx):
    await ctx.send(f'_!command_ _number_ _number_    For example, you want to add numbers, you have to use **!add 1 1** command. So you have to type the command first then type the numbers you want to add.')

@bot.command
async def game(ctx):
    botnumber = gm.oyun()
    usernumber = ctx.send(input("Guess the number!"))
    if usernumber == botnumber:
        await ctx.send("Correct!")
    else:
        await ctx.send("Wrong...")

bot.run(" TOKEN HERE ")