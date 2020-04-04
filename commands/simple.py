import discord
from discord import Message
from discord.ext import commands

async def hello(self, message:Message):
    await message.channel.send(f'Hello {message.author.mention}')

async def mentioned(self, message: Message):
    await message.channel.send(f'I was mentioned!?')

async def what(self, message: Message):
    await message.channel.send(f'Sorry, I didn\'t quite understand that!')