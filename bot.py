# bot.py
import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
# this is the code we will use first to test the connection
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('Hello Mr. Botface'):
    await message.channel.send('Howdy Stranger')
# start the bot
client.run(TOKEN)
