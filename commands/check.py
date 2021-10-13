import json
import urllib.request
from re import match
from typing import Sequence
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord.utils import get
from difflib import *
import core.hypixel as hypixel
import os

API_KEYS = [os.environ['API_KEY']]
hypixel.setKeys(API_KEYS)

class Test(Cog_Extension):
    @commands.command()
    async def check(self,ctx):
          await ctx.send(f"{ctx.message.author.mention} Checking......")
          nickname = ctx.message.author.display_name
          if SequenceMatcher(None, nickname, "<").ratio() == 0 or SequenceMatcher(None, nickname, ">").ratio() == 0:
              await ctx.send("暱稱格式不正確\n請改為暱稱<Minecraft ID>")
          else:
              id = nickname.split('<')
              id1 = id[1].split('>')
              await ctx.send(f"Minecraft ID : {id1[0]}")
              if id1[0] != "no ID":
                  resource_url = 'https://api.mojang.com/users/profiles/minecraft/' + id1[0]
                  getPlayerUUID = json.loads(urllib.request.urlopen(resource_url).read())
                  playerUUID = getPlayerUUID['id']
                  player = hypixel.Player(playerUUID)
                  playerRank = player.getRank()
                  await ctx.send(f"Hypixel Rank : " + playerRank['rank'])
                  memberRankRole = discord.utils.get(ctx.guild.roles, name=playerRank['rank'])
                  await ctx.author.add_roles(memberRankRole)
                  await ctx.send(f"Hypixel Rank身分組成功增加")
                  #公會ID
                  playerGuildID = player.getGuildID()
                  if playerGuildID is not None:
                      guild = hypixel.Guild(playerGuildID)
                      playerGuildData = guild.JSON
                      playerGuildName = str(playerGuildData['name'])
                      await ctx.send(f"目前所在公會 : " + playerGuildName)
                      print(playerGuildName)
                      try:
                          memberGuildRole = discord.utils.get(ctx.guild.roles, name=playerGuildName)
                          print(playerGuildName)
                      except:
                          print(playerGuildName)
                          guild = bot.get_guild(518290953908518922)
                          await guild.create_role(name = 'awd')
                          print(playerGuildName)
                          memberGuildRole = discord.utils.get(ctx.guild.roles, name=playerGuildName)
                      await ctx.author.add_roles(memberGuildRole)
                      await ctx.send(f"公會身分組成功增加")
                      if playerGuildName == 'HelloTaiwan':
                          memberRoleName = '普通會員<Member>'
                          print(memberRoleName)
                      else:
                          memberRoleName = '🌈好捧油🌈<Friend>'
                          print(memberRoleName)
                  else:
                      await ctx.send(f"查無公會")
                      memberRoleName = '🌈好捧油🌈<Friend>'
                  #DC身分組增加
                  memberRole = discord.utils.get(ctx.guild.roles, name=memberRoleName)
                  await ctx.author.add_roles(memberRole)
                  await ctx.send(f"DC身分組成功增加\nHaving Fun :U")

def setup(bot):
    bot.add_cog(Test(bot))
