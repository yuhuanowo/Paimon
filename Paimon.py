#need discod.py
from encodings import utf_8
import imp
import discord #導入discord.py
from discord.ext import commands
import json #導入json
import random #隨機挑選
import os 

with open("setting.json","r",encoding="utf8") as jfile: #開啟檔案(json)(utf8解碼)
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True #網關意圖


bot = commands.Bot (command_prefix="~",intents = intents) 
#指令前綴

@bot.event#bot上線提醒
async def on_ready():
    print(">>bot is online<<")

@bot.event#成員加入
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(F"@{member}join!")


@bot.event#成員退出
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(F"{member}leave!")

@bot.command()#ping
async def ping(ctx):
   await ctx.send(f"{round(bot.latency*1000)}(ms)")

@bot.command()#fat
async def fat(ctx):
   await ctx.send("白白最胖")

@bot.command()#傳送圖片 
async def 圖片(ctx):
    pic = discord.File(jdata["pic"]) #\\強制便路徑
    await ctx.send(file= pic)


bot.run(jdata["TOKEN"]) #回傳文件裡面的TOKEN



#ctx:上下文-回復(包含人.頻道)
#jdata["name"]
