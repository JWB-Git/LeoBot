import os
import random
import requests
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

## USEFUL FUNCTIONS ##
def dataRequest(path):
    url = BASE_URL + path
    r = requests.get(url = url)
    return r.json()

## BASIC TEXT COMMANDS ##
bot = commands.Bot(command_prefix='!')

@bot.command(name='leo')
async def leo(ctx, arg: str):
    if arg == "hi":
        await ctx.send(
            f'Hi {ctx.author.mention}!'
        )

    elif arg == "sally":
        await ctx.send(
            f'Sally (:sally:) is my Best Friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:'
        )

    elif arg == "git":
        await ctx.send(
            f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever seen but theres a computer behind me!' +
            '\n' +
            'https://github.com/JWB-Git/LeoBot'
        )

    elif arg == "rally":
        await ctx.send(
            f'Did you know my friends from NUSSAGG and DUSSAG are hosting Viking Rally in November 2021! Please come join us for a weekend of great fun in the Toon '+
            'and surrounding areas. Its a canny place to be!'
        )

    elif arg == "steal":
        await ctx.send(
            f'You can\'t steal me! Sally (:sally:) is NUSSAGG\'s stealable mascot!'
        )

    elif arg == "adventure":
        mascotData = dataRequest('read/mascots.php')
        locationData = dataRequest('read/locations.php')

        if mascotData['success'] == 1 and locationData['success'] == 1:
            mascots = mascotData['mascots']
            locations = locationData['locations']

            mascot = random.choice(mascots)
            location = random.choice(locations)

            await ctx.send(
                f'I want to go to {location} with {mascot} on my next adventure! :airplane:'
            )
        else:
            await ctx.send(f'I don\'t know where I would like to visit next right now, but ask me again later!')

    elif arg == "memory":
        data = dataRequest('read/memories.php')

        if data['success'] == 1:
            memories = data['memories']
            memory = random.choice(memories)
            await ctx.send(memory)
        else:
            await ctx.send(f'I can\'t seem to remember anything at the minute :tired_face:. Please try again later!')

    else:
        await ctx.send(f'I don\'t understand you!') 

@bot.command(name='roar', help='Make Leo Roar!')
async def roar(ctx, length: int):
    if length == 69:
        await ctx.send(f':rolling_eyes:')
    elif length > 999:
        await ctx.send(f'I can\'t roar for that long!')
    else:
        roar_str = 'R'
        for i in range(length):
            roar_str += 'o'
        for i in range(length):
            roar_str += 'a'
        roar_str += 'r'

        await ctx.send(roar_str)
    
bot.run(TOKEN)