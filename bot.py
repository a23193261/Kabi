import discord
from discord import channel
from discord.ext import commands
import json
import random
import os

from discord.file import File 

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f"@{member} 滑進了伺服器 !")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f" @{member} 滑出了伺服器 !")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded{extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un_loaded{extension} done.')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re_loaded{extension} done.')



for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')





if __name__== "__main__":
    bot.run(jdata['token'])