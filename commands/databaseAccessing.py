import discord
from discord import Message
from discord.ext import commands

import json
import requests
import random

import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

#Returns JSON from Database API Calls
def dataRequest(path):
    url = BASE_URL + path
    r = requests.get(url = url)
    return r.json()

async def memory(self, message: Message):
    data = dataRequest('read/memories.php')

    if data['success'] == 1:
        memories = data['memories']
        memory = random.choice(memories)
        await message.channel.send(memory)
    else:
        await message.channel.send(f'I can\'t seem to remember anything at the minute :tired_face:. Please try again later!')

async def adventure(self, message: Message):
    mascotData = dataRequest('read/mascots.php')
    locationData = dataRequest('read/locations.php')

    if mascotData['success'] == 1 and locationData['success'] == 1:
        mascots = mascotData['mascots']
        locations = locationData['locations']

        mascot = random.choice(mascots)
        location = random.choice(locations)

        await message.channel.send(f'I want to go to {location} with {mascot} on my next adventure! :airplane:')
    else:
        await message.channel.send(f'I don\'t know where I would like to visit next right now, but ask me again later!')