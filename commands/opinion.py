import discord
from discord import Message
from discord.ext import commands

async def opinion(self, message: Message):
    if len(message.mentions) == 1:
        await message.channel.send(f'I can\'t give an opinion on myself')
        return

    tagged = message.mentions[1]

    #Specific SSAGO Server Roles
    mascot = discord.utils.get(message.guild.roles, name="Mascot")
    execMascot = discord.utils.get(message.guild.roles, name="Exec Mascot")
    execMember = discord.utils.get(message.guild.roles, name="Exec")
    nussagg = discord.utils.get(message.guild.roles, name="NUSSAGG")

    #Specific SSAGO Members - Not in the assets file because python import
    #where being weird.
    jackId = 311556785498619904
    erinId = 689574093040779293
    nussaggPresidentId = 689742684239298572
    ellieId = 689661254788448265
    ellieId = 696051357567811614
    timId = 689579955012632586

    #Jack - Owner and Creator
    if tagged.id == jackId:
        await message.channel.send(f'I love {tagged.mention}, after all, he programmed my speech!')
    
    #Erin - Requested Leo as a follower
    elif tagged.id == erinId:
        await message.channel.send(f'{tagged.mention} is my favourite Scot and should be yours too!')
    
    #NUSSAGG President
    elif tagged.id == nussaggPresidentId:
        await message.channel.send(f'Of course I love el presidente of NUSSAGG. {tagged.mention} is our coolest president since our last one!')

    #Ellie - The normal guardian of Leo
    elif tagged.id == ellieId:
        await message.channel.send(f'{tagged.mention} is the one who normally looks after me on and off events! I even met her neighbours cat!')
    
    #Tim - NUSSAGG old timmer
    elif tagged.id == timId:
        await message.channel.send(f'Whilst I love {tagged.mention}, after all he was President of NUSSAGG for 3 years,'
                                   f' he\'s definitely an old timer! Will he ever leave NUSSAGG :rolling_eyes:')

    #Other Bot Mascots
    elif mascot in tagged.roles or execMascot in tagged.roles:
        await message.channel.send(f'{tagged.mention} is a bot just like me, so is pretty cool')
    
    #Exec Memebers
    elif execMember in tagged.roles:
        await message.channel.send(f'I like {tagged.mention} as they keep SSAGO going with the rest of the Exec! :smiley:')

    #NUSSAGG Members
    elif nussagg in tagged.roles:
        await message.channel.send(f'{tagged.mention} looks after me well, I\'m  glad they are part of NUSSAGG!')
    
    #Everyone else
    else:
         await message.channel.send(f'{tagged.mention} is pretty cool')