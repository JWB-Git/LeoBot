import os
import random
import requests
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

bot = commands.Bot(command_prefix='!')

## BASIC TEXT COMMANDS ##
@bot.command(name='hi', help='Leo says hi')
async def hi_leo(ctx):
    await ctx.send(
        f'Hi {ctx.author.mention}!'
    )

@bot.command(name='sally', help='Info about Sally the Seahorse')
async def sally(ctx):
    await ctx.send(
        f'Sally is my Best Friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:'
    )

@bot.command(name='git', help='Link to the Git Repo')
async def git(ctx):
    await ctx.send(
        f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever seen but theres a computer behind me!' +
        '\n' +
        'https://github.com/JWB-Git/LeoBot'
    )

@bot.command(name='rally', help='Info about viking rally')
async def rally(ctx):
    await ctx.send(
        f'Did you know my friends from NUSSAGG and DUSSAG are hosting Viking Rally in November 2021! Please come join us for a weekend of great fun in the Toon '+
        'and surrounding areas. Its a canny place to be!'
    )

@bot.command(name='adventure', help='Generates an adventure Leo wants to go on')
async def adventure(ctx):
    mascots = ['Sally', 'Hamish', 'Conker', 'Harold', 'Gossy']

    locations = ['Hull', 'York', 'Glasgow', 'Edinburgh',
                'Leicester', 'Bath', 'Durham', 'Sheffield',
                'London', 'The Seaside', 'Outer Space', 'Leeds',
                'Manchester', 'Swansea', 'Southampton']

    mascot = random.choice(mascots)
    location = random.choice(locations)

    await ctx.send(
        f'I want to go to {location} with {mascot} on my next adventure! :airplane:'
    )

@bot.command(name='memory', help='Leo says a random memory of his')
async def memory(ctx):
    url = BASE_URL + 'read/memories.php'
    r = requests.get(url = url)
    data = r.json()
    memories = data['memories']

    memory = random.choice(memories)

    await ctx.send(memory)

@bot.command(name='roar')
async def roar(ctx, length: int):
    if length > 999:
        await ctx.send('I can\'t roar for that long!')
    else:
        roar_str = 'R'
        for i in range(length):
            roar_str += 'o'
        for i in range(length):
            roar_str += 'a'
        roar_str += 'r'

        await ctx.send(roar_str)
    
bot.run(TOKEN)