import os
import logging
from dotenv import load_dotenv
from discord.ext import commands
import discord
from pretty_help import PrettyHelp
from cogs import basic, data_access
from constants import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set up error logger
logger = logging.getLogger('Discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename=os.path.join(os.curdir, 'discord.log'), encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()


class Leo(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        commands.Bot.__init__(self, command_prefix=commands.when_mentioned_or("Leo "), case_insensitive=True,
                              help_command=PrettyHelp(color=discord.Color.purple, show_index=False), intents=intents)

        # Add Cogs Here
        self.add_cog(basic.Basic())
        self.add_cog(data_access.DataAccess())


    # Set Activity
    async def on_ready(self):
        await commands.Bot.change_presence(self, activity=discord.Activity(type=discord.ActivityType.listening,
                                                                           name="Blaydon Races"))

    # Send Errors to Log
    async def on_command_error(self, ctx, exception):
        print(exception)
        if isinstance(exception, commands.errors.MissingRequiredArgument):  # Capture for missing argument error
            await ctx.send(
                'Oh nee!, You\'ve missed a required argument for this command! This command will have its own'
                ' help argument, so type it again with help before it!')
        elif isinstance(exception,
                        commands.errors.MissingRole):  # Capture for the missing role error (e.g. for 'say')
            await ctx.send(
                f"Oh nee!, You don't have the correct permissions to do that - naughty {ctx.author.mention}!")
        else:
            await ctx.send('Oh nee!, somethings gone wrong here. You\'ve either encountered a bug or the command you'
                           ' entered dosen\'t exist! I\'ve sent more info about what\'s gone wrong to my developers so'
                           ' they can work this out')

        # Send Error Info to Jack in a DM
        jack = self.get_user(JACK_USER_ID)

        embed = discord.Embed(
            title="An error has occured!",
            color=discord.Color.dark_blue(),

        )

        embed.add_field(
            name="Message",
            value=ctx.message.content,
            inline=False
        )
        embed.add_field(
            name="Author",
            value=ctx.author,
            inline=False
        )
        embed.add_field(
            name="Channel",
            value=ctx.channel,
            inline=True
        )
        embed.add_field(
            name="Guild",
            value=ctx.guild,
            inline=True
        )
        embed.add_field(
            name="Error",
            value=exception,
            inline=False
        )

        await jack.send(embed=embed)


# Load token from .env
TOKEN = os.getenv('DISCORD_TOKEN')

# Run Bot
leo = Leo()
leo.run(TOKEN)
