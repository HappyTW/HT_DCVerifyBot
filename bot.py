import discord
import requests
import json
import os
from discord.ext import commands

activity = discord.Streaming(name="!help | !check進行身分認證", url="https://www.twitch.tv/")
bot = commands.Bot(os.environ['prefix'], activity=activity, status=discord.Status.idle)

@bot.event
async def on_ready():
    print('澳門首家ㄐㄐ賭場上線啦')

for fileName in os.listdir('./commands'):
    if fileName.endswith('.py'):
        bot.load_extension(f'commands.{fileName[:-3]}')

if __name__ == "__main__":
    bot.run(os.environ['token'])
