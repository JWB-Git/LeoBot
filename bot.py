import os
import random
import requests
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SSAGO_SERVER')
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

bot = commands.Bot(command_prefix='?') #All commands will start with !

previousPhrase = ""

## USEFUL FUNCTIONS ##
#Returns JSON from Database API Calls
def dataRequest(path):
    url = BASE_URL + path
    r = requests.get(url = url)
    return r.json()

#Method for an invalid call message
async def invalidCommand(ctx):
    await ctx.send(f'I don\'t understand you! Type \'?leo help\' to learn what I can do')

## BASIC TEXT COMMANDS ##

# Replies every time Erin messages - As requested by Erin XD
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.id == 689574093040779293:
        await message.channel.send('Hi Erin :scotland:!')

    await bot.process_commands(message)

@bot.command(name='leo')
async def leo(ctx, *args: str):
    if len(args) == 1:
        arg = args[0]
        
        # ?leo help
        if arg == "help":
            embed = discord.Embed(title="Leo the Lion Help", description="Available Commands:", colour=0x7413dc)
            
            embed.add_field(name="?leo hi", value="Leo will say hi to you!")
            embed.add_field(name="?leo sally", value="Leo will talk about Sally the Seahorse")
            embed.add_field(name="?leo git", value="A link to the LeoBot git will be sent")
            embed.add_field(name="?leo rally", value="Leo will talk about Viking Rally")
            embed.add_field(name="?leo steal", value="Try and steal leo, but it won't end well!")
            embed.add_field(name="?leo drink", value="Leo will take a drink")
            embed.add_field(name="?leo adventure", value="Leo will say what adventure he wants to go on next!")
            embed.add_field(name="?leo memory", value="Leo will tell you one of his favourite memories with NUSSAGG")
            embed.add_field(name="?leo geordie", value="Leo will say some geordie")
            embed.add_field(name="?leo translate", value="Leo will translate the geordie he just said")
            embed.add_field(name="?leo roar <length>", value="Leo will roar for the length specified (up to a value of 999)")
            embed.add_field(name="?leo opinion <user>", value="Leo will say his opinion on the tagged person")

            await ctx.send(embed = embed)

        # ?leo hi
        elif arg == "hi":
            await ctx.send(
                f'Hi {ctx.author.mention}!'
            )

        # ?leo sally
        elif arg == "sally":
            await ctx.send(
                f'Sally (<:Sally:689616621576257557>) is my Best Friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:'
            )

        #?leo git
        elif arg == "git":
            await ctx.send(
                f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever seen but theres a computer behind me!' +
                '\n' +
                'https://github.com/JWB-Git/LeoBot'
            )

        # ?leo rally
        elif arg == "rally":
            await ctx.send(
                f'Did you know my friends from NUSSAGG and DUSAGG are hosting Viking Rally in November 2021! Please come join us for a weekend of great fun in the Toon '+
                'and surrounding areas. Its a canny place to be!'
            )
        # ?leo steal
        elif arg == "steal":
            await ctx.send(
                f'You can\'t steal me! Sally (<:Sally:689616621576257557>) is NUSSAGG\'s stealable mascot!'
            )

        # ?leo drink
        elif arg == "drink":
            await ctx.send(
                f'Cheers! :beers:'
            )

        # ?leo adventure
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

        # ?leo memory
        elif arg == "memory":
            data = dataRequest('read/memories.php')

            if data['success'] == 1:
                memories = data['memories']
                memory = random.choice(memories)
                await ctx.send(memory)
            else:
                await ctx.send(f'I can\'t seem to remember anything at the minute :tired_face:. Please try again later!')

        # ?leo geordie
        elif arg == "geordie":
            data = dataRequest('read/phrases.php')

            if data['success'] == 1:
                phrases = data['phrases']
                phrase = random.choice(phrases)
                global previousPhrase
                previousPhrase = phrase['id']
                await ctx.send(phrase['geordie'])
            else:
                await ctx.send(f'I can\'t seem to remember anything at the minute :tired_face:. Please try again later!')

        # ?leo translate
        elif arg == "translate":
            if previousPhrase == "":
                await ctx.send(f'I haven\'t said any geordie to translate!')
            else:
                requestPath = "read/translate.php?id=" + previousPhrase
                data = dataRequest(requestPath)

                if data['success'] == 1:
                    translation = data['translation']
                    usage = data['usage']
                    await ctx.send(
                        f'Translation: {translation} \nUsage: {usage}'
                    )
                else:
                    ctx.send(f'I can\'t translate right now!')

        else:
            await invalidCommand(ctx)

    elif len(args) == 2:
        arg1 = args[0]
        arg2 = args[1]

        # ?leo test
        if arg1 == "opinion":
            if arg2.index("@") == 1: #Indicates it is a username
                tagged = ctx.message.mentions[0]

                #Special Cases

                #Specific ID's
                jackId = 311556785498619904
                erinId = [691030078762778674, 689574093040779293]
                nussaggIds = [689742684239298572, 689579955012632586, 689805495988781074]

                #Specific Roles
                mascot = discord.utils.get(ctx.message.guild.roles, name="Mascot")
                execMascot = discord.utils.get(ctx.message.guild.roles, name="Exec Mascot")
                execMember = discord.utils.get(ctx.message.guild.roles, name="Exec")

                if tagged.id == jackId:
                    await ctx.send(f'I love {tagged.mention}, after all, he programmed my speech!')
                elif tagged.id in erinId:
                    await ctx.send(f'{tagged.mention} is my favourite Scot and should be yours too!')
                elif tagged.id in nussaggIds:
                    await ctx.send(f'{tagged.mention} looks after me well, I\'m  glad they are part of NUSSAGG!')
                elif mascot in tagged.roles or execMascot in tagged.roles:
                    await ctx.send(f'{tagged.mention} is a bot just like me, so is pretty cool')
                elif execMember in tagged.roles:
                    await ctx.send(f'I like {tagged.mention} as they keep SSAGO going with the rest of the Exec! :smiley:')

                #Normal Cases
                else:
                    await ctx.send(f'{tagged.mention} is pretty cool')

            else:
                await ctx.send(f'I\'m sorry, I don\'t know this person :frowning:')

        elif arg1 == "roar":
            length = int(arg2)

            #Special Cases
            if length == 69:
                await ctx.send(f':rolling_eyes:')
            elif length == 666:
                await ctx.send(f':japanese_ogre:')
            elif length <= 0:
                await ctx.send(f'How would I roar for zero or negative length!?')
            elif length > 999:
                await ctx.send(f'I can\'t roar for that long!')

            #Normal Roar
            else:
                roar_str = 'R'
                for i in range(length):
                    roar_str += 'o'
                for i in range(length):
                    roar_str += 'a'
                roar_str += 'r'

                await ctx.send(roar_str)

        else:
            await invalidCommand(ctx)

    else:
        await invalidCommand(ctx)
    
bot.run(TOKEN)