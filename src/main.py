import discord
from ai import run_ai
import os

bot = discord.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
   print("Bot is online")

@bot.event
async def on_message(message):
   if message.author == bot.user:
        return
   if bot.user in message.mentions:
        response = run_ai(message.content, message.author)
        await message.channel.send(response)

bot.run(os.environ.get("BOT_TOKEN"))
