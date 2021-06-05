import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands.core import command

class Cog_Extension(commands.Cog):
        def __init__(self,bot):
            self.bot = bot