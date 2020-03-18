import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

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
    memories = [
        'I loved eating all the chocolate at Cadbury World when I went to Birmingham Chocolate Rally',
        'I enjoyed exploring Bath on the Roman Rally Monopoly Run',
        'I had great fun help run a Monopoly Run for City of Newcastle Scouts!',
        'I really liked going to the North Tyneside coast, even if it was cold and windy!',
        'I loved visiting Beamish and riding on the trams!',
        'I had an amazing time at Northern Freshers in Hull, seeing Sally\'s Brothers and Sisters in the Deep'
    ]

    memory = random.choice(memories)

    await ctx.send(memory)
    
bot.run(TOKEN)