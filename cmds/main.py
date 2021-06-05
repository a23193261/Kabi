from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"現在的網路延遲是 {round(self.bot.latency*1000)} ms ! ")

def setup(bot):
    bot.add_cog(Main(bot))