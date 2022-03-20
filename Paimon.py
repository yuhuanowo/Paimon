#need discod.py
from encodings import utf_8
import imp
from sqlite3 import Timestamp
import discord #導入discord.py
from discord.ext import commands
import json #導入json
import random #隨機挑選
import os #cog
import datetime #系統標準時間
import asyncio #異步執行

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

@bot.event #處理指令錯誤
async def on_command_error(ctx,error):
    await ctx.send(error)

@bot.event#說出fuck傳fuck
async def on_message(message):
    if message.content == "fuck"and message.author != bot.user:
        await message.channel.send('fuck')
    await bot.process_commands(message)


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

@bot.command()#崁入介面
async def em(ctx):
    embed=discord.Embed(title="About", url="https://live.bilibili.com/363889?broadcast_type=0&spm_id_from=333.788.top_right_bar_window_dynamic.content.click", description="about this bot", color=0xff8ae6,timestamp= datetime.datetime.utcnow())
    embed.set_author(name="Paimon")
    embed.set_thumbnail(url="https://uploadstatic-sea.hoyoverse.com/contentweb/20220215/2022021519402058141.png")
    embed.add_field(name="1", value="fuck", inline=True)
    embed.add_field(name="2", value="lol", inline=True)
    embed.add_field(name="3", value="fat", inline=True)
    embed.set_footer(text="made by Paimon")
    await ctx.send(embed=embed)

@bot.command()#say幫你說
async def say(ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg)

#@bot.command()
#async def clean(ctx,number:int):
#    await ctx.channel.purge(limit=number+1)
#清訊息 先暫停





bot.run(jdata["TOKEN"]) #回傳文件裡面的TOKEN



#ctx:上下文-回復(包含人.頻道)
#jdata["name"]