import discord
from discord.ext import commands


bot = commands.Bot (command_prefix="!") 
#or if you realize that you forgot a capital 'B' so it's like accessing the module in that way without a capital 'B'

@bot.event
async def on_ready():
    print(">>bot is online<<")

bot.run("OTQ1NjIyODA1NzQ2MTYzNzEy.YhS13Q.HnPCISRWhO7ZLSFzVyKRUUE1INI")
