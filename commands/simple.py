import discord
from discord import Message
from discord.ext import commands

from assets.constants import SALLY_TAG, SALLY_EMOJI, JAMES_TAG

async def hello(self, message: Message):
    await message.channel.send(f'Hello {message.author.mention}')

async def git(self, message: Message):
    await message.channel.send(
        f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever seen but theres a computer behind me!' +
        '\n' +
        'https://github.com/JWB-Git/LeoBot'
    )

async def mentioned(self, message: Message):
    await message.channel.send(f'I was mentioned!?')

async def what(self, message: Message):
    await message.channel.send(f'Sorry, I didn\'t quite understand that! Type @Leo The Lion help for my commands')

async def sally(self, message: Message):
    await message.channel.send(f'{SALLY_TAG} {SALLY_EMOJI} is my best friend! We go on all our adventures together but we have to protect her, as other SSAGOers like to steal her! :frowning:')

async def insta(self, message: Message):
    await message.channel.send(
        f'Here is {SALLY_TAG} {SALLY_EMOJI} and mine Instagram. Make sure you give us a follow!' +
        '\n' +
        'https://www.instagram.com/nussaggsallyandleo/'
    )

async def rally(self, message: Message):
    await message.channel.send(f'Did you know my friends from NUSSAGG and DUSAGG are hosting Viking Rally in November 2021! Please come join us for a weekend of great fun in the Toon and surrounding areas. Its a canny place to be!')

async def steal(self, message: Message):
    await message.channel.send(f'You can\'t steal me! {SALLY_TAG} {SALLY_EMOJI} is NUSSAGG\'s stealable mascot!')

async def drink(self, message: Message):
    await message.channel.send(f'Cheers! :beers:')

async def favouriteFood(self, message: Message):
    await message.channel.send(f'My favourite food is Lamb so you better run {JAMES_TAG}! :drool:')

async def say(self, say: str, message: Message):
    await message.channel.send(say)

async def roar(self, length: int, message: Message):
    roar = ""

    #Special Cases
    if length == 69:
        roar = ':rolling_eyes:'
    elif length == 666:
        roar = ':japanese_ogre:'
    elif length <= 0:
        roar = 'How would I roar for zero or negative length!?'
    elif length > 999:
        roar = 'I can\'t roar for that long!'

    #Normal Roar
    else:
        roar = 'R'
        for i in range(length):
            roar += 'o'
        for i in range(length):
            roar += 'a'
        roar += 'r'

    await message.channel.send(roar)