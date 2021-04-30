from discord.ext import commands
import discord
import json
import random


class DataAccess(commands.Cog):
    @commands.command(name="crossover", brief="Generate a SSAGO Club Crossover Event",
                      help="Generate a SSAGO Club Crossover Event")
    async def crossover(self, ctx):
        with open("data.json") as f:
            data = json.load(f)

        club1 = data['clubs'][random.randrange(0, len(data['clubs']))]
        club2 = data['clubs'][random.randrange(0, len(data['clubs']))]
        activity = data['activities'][random.randrange(0, len(data['activities']))]

        await ctx.send(f"{club1} and {club2} {activity}")

    @commands.command(name="geordie", brief="I'll tell you all about a Geordie phrase",
                      help="I'll tell you all about a Geordie phrase")
    async def geordie(self, ctx):
        with open("data.json") as f:
            data = json.load(f)

        phrase_obj = data["phrases"][random.randrange(0, len(data["phrases"]))]
        embed = discord.Embed(
            title=phrase_obj["geordie"],
            color=discord.Color.dark_blue()
        )
        embed.add_field(
            name="Translation",
            value=phrase_obj["translation"]
        )
        embed.add_field(
            name="Usage",
            value=phrase_obj["phrase_usage"]
        )

        await ctx.send(embed=embed)
