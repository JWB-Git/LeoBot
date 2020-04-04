import discord
from discord import Message
from discord.ext import commands

from commands.databaseAccessing import dataRequest

import json
import requests
import random

import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

def randomGeordie():
    data = dataRequest('read/phrases.php')

    if data['success'] == 1:
        phrases = data['phrases']
        return random.choice(phrases)

async def translate(self, id, message: Message):
    requestPath = "read/translate.php?id=" + id
    data = dataRequest(requestPath)

    if data['success'] == 1:
        translation = data['translation']
        usage = data['usage']
        await message.channel.send(
            f'Translation: {translation} ' +
            f'\n' +
            f'Usage: {usage}'
        )
    else:
        message.channel.send(f'I can\'t translate right now!')