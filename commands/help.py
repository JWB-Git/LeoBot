import discord
from discord import Message
from discord.ext import commands

from assets.constants import SALLY_EMOJI

async def commandList(self, message: Message):
    embed = discord.Embed(title="Leo the Lion Help", description="@Leo the Lion", colour=0x7413dc)
            
    embed.add_field(name="hi", value="Leo will say hi to you!")
    embed.add_field(name="sally", value=f"Leo will talk about Sally the Seahorse {SALLY_EMOJI}")
    embed.add_field(name="git", value="A link to the LeoBot git will be sent")
    embed.add_field(name="insta", value=f"A link to Leo and Sally's {SALLY_EMOJI} Instagram will be sent")
    embed.add_field(name="rally", value="Leo will talk about Viking Rally")
    embed.add_field(name="steal", value="Try and steal leo, but it won't end well!")
    embed.add_field(name="drink", value="Leo will take a drink")
    embed.add_field(name="adventure", value="Leo will say what adventure he wants to go on next!")
    embed.add_field(name="memory", value="Leo will tell you one of his favourite memories with NUSSAGG")
    embed.add_field(name="geordie", value="Leo will say some geordie")
    embed.add_field(name="translate", value="Leo will translate the geordie he just said")
    embed.add_field(name="roar <length>", value="Leo will roar for the length specified (up to a value of 999)")
    embed.add_field(name="opinion <user>", value="Leo will say his opinion on the tagged person")

    await message.channel.send(embed = embed)