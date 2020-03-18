import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

## BASIC TEXT COMMANDS ##
@bot.command(name='hi')
async def hi_leo(ctx):
    await ctx.send(
        f'Hi {ctx.author.mention}!'
    )

@bot.command(name='sally')
async def sally(ctx):
    await ctx.send(
        f'Sally is my Best Friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:'
    )

@bot.command(name='git')
async def git(ctx):
    await ctx.send(
        f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever seen but theres a computer behind me!' +
        '\n' +
        'https://github.com/JWB-Git/LeoBot'
    )

@bot.command(name="rally")
async def rally(ctx):
    await ctx.send(
        f'Did you know my friends from NUSSAGG and DUSSAG are hosting Viking Rally in November 2021! Please come join us for a weekend of great fun in the Toon '+
        'and surrounding areas. Its a canny place to be!'
    )

@bot.command(name="adventure")
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
    
bot.run(TOKEN)