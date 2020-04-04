import discord
from discord import Message
from discord.ext import commands

import os
from dotenv import load_dotenv

#Command Imports
from commands.simple import *
from commands.help import *
from commands.databaseAccessing import adventure, memory
from commands.geordie import randomGeordie, translate
from commands.opinion import opinion

#Asset Imports (Constants etc.)
from assets.constants import SALLY_TAG, ERIN_ID

class LeoTheLion(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.previousPhrase = ""

    async def on_message(self, message: Message):
        if message.author == client.user:
            return

        #Ignore Sally
        if message.author.display_name == "SallyBot":
            return

        #Leo is mentioned
        if message.mentions and message.mentions[0].name == 'Leo the Lion':
            #Get Arguments
            args = message.content[22:].lower().strip().split(" ")
            print(args)

            #One Argument Commands
            if len(args) == 1:
                arg = args[0]

                if arg == "":
                    await mentioned(self, message)

                elif arg == "help" or arg == "commands":
                    await commandList(self, message)

                elif arg == "hello" or arg == "hi":
                    await hello(self, message)

                elif arg == "git" or arg=="brain":
                    await git(self, message)

                elif arg == "sally" or arg == SALLY_TAG:
                    await sally(self, message)

                elif arg == "insta" or arg == "instagram":
                    await insta(self, message)

                elif arg == "rally":
                    await rally(self, message)

                elif arg == "steal":
                    await steal(self, message)

                elif arg == "drink":
                    await drink(self, message)

                elif arg == "adventure":
                    await adventure(self, message)

                elif arg == "memory":
                    await memory(self, message)

                elif arg == "geordie":
                    self.previousPhrase = randomGeordie()
                    await say(self, self.previousPhrase['geordie'], message)

                elif arg == "translate":
                    if self.previousPhrase != "":
                        await translate(self, self.previousPhrase['id'], message)
                    else:
                        await message.channel.send(f'I haven\'t said any geordie to translate!')

                else:
                    await what(self, message)

            #Two Argument Commands
            elif len(args) == 2:
                arg1 = args[0]
                arg2 = args[1]

                if arg1 == "roar":
                    try:
                        length = int(arg2)
                        await roar(self, length, message)
                    except ValueError:
                        await message.channel.send(f'I can\'t roar for a non integer length!')

                elif arg1 == "opinion":
                    if "<@!" in arg2: #Indicates tagged user in arg2
                        await opinion(self, message)
                    else:
                        await message.channel.length(f'I\'m sorry, I don\'t know this person :frowning:')

                else:
                    await what(self, message)

            else:
                await what(self, message)

        #Other responces

        #Responds to James the Sheep Running Away
        if message.content == "baaaaaa, run away!":
            await favouriteFood(self, message)

        if message.author.id == ERIN_ID:
            await message.channel.send('Hi Erin :scotland:!')

#Load Secrets
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Create and Run Leo
client = LeoTheLion()
client.run(TOKEN)
