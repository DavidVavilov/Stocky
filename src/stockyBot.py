import requests
import json
import discord
import stocky
import cran
from discord.ext import commands 
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


client = commands.Bot(command_prefix = "!")

TOKEN = cran.TOKEN

@client.event
async def ready():
    print("Bot is online")

'''@wa.error
async def info_error(ctx, error):
    if MissingRequiredArgument:
        await ctx.send('u dumb ass u need to type a name')'''

@client.command()
async def stockyy(ctx):
    await ctx.send("Its me, Stocky")

@client.command()
async def stock(ctx, *, company):
      print(company)
      date, stock, emote = stocky.todayStock(company)
      await ctx.send(f"{company.upper()} - Stock - {format(round(stock, 2))}, Date - {date} {emote}")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"{error}")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"{error}")


    
client.run(TOKEN)
