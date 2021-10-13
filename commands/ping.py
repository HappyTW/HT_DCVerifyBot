import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Ping(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

def setup(bot):
    bot.add_cog(Ping(bot))
