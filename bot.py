import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hi leo' in message.content.lower():
        await message.channel.send(f'Hi {message.author.mention}!')

    if message.content.startswith('!sally'):
        await message.channel.send(
            f'Sally is my Best Friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:'
        )
    
client.run(TOKEN)