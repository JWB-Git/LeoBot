import discord
from discord import Message
from discord.ext import commands

import json
import requests

import os
from dotenv import load_dotenv

from commands.databaseAccessing import dataRequest

load_dotenv()
BASE_URL = os.getenv('BASE_URL') #Base URL for API Calls

from assets.constants import LEO_ID, PARTY_RING_EMOJI

async def partyRing(self, message: Message):
    await message.channel.send(f"I'm on Team Party Ring {PARTY_RING_EMOJI}! Type '<@{LEO_ID}> Party Ring Join' to join Team Party Ring!")

async def joinPartyRing(self, message):
    person = message.author

    url = BASE_URL + "write/team_party_ring.php"
    r = requests.post(url= url, data={'person' : person.id})

    responce = r.json()
    if responce['success'] == 1:
        await message.channel.send(f"{person.mention}, Your now a member of Team Party Ring {PARTY_RING_EMOJI}!")
    else:
        await message.channel.send(f"Oops, something has gone wrong. Maybe your already a member of Team Party Ring?")

async def membersPartyRing(self, message):
    membersData = dataRequest("read/team_party_ring.php")

    if membersData['success'] == 1:
        members = membersData['members']

        output = f"These are the members of Team Party Ring {PARTY_RING_EMOJI}:\n"
        output += f"{PARTY_RING_EMOJI} <@{LEO_ID}>\n"

        for member in members:
            output += f"{PARTY_RING_EMOJI} <@{member}>\n"

        await message.channel.send(output)

    else:
        await message.channel.send(f"Oops, I can't remember any members of Team Party Ring {PARTY_RING_EMOJI} right now!")
    

