from discord.ext import commands
from constants import *
import math
import random


class Basic(commands.Cog):
    @commands.command(name="hello", aliases=["hi", "whyaye"], brief="Say Hello to Leo", help="Say Hello to Leo")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention} from Rewrite")

    @commands.command(name="git", brief="Have a look at my code", help="A link to may git repo")
    async def git(self, ctx):
        await ctx.send(
            f'Here\'s the git repo that contains all my inner code. I may look like the best teddy lion you\'ve ever'
            f'seen but there is a computer behind me!'
            '\n'
            'https://github.com/JWB-Git/LeoBot'
        )

    @commands.command(name="sally", brief="Learn more about Sally", help="Learn more about Sally")
    async def sally(self, ctx):
        await ctx.send(f"{SALLY_TAG} {SALLY_EMOJI} is my best friend, but people keep on trying to steal her!")

    @commands.command(name="roar", brief="Make Leo Roar!", help="Make Leo Roar")
    async def roar(self, ctx, length):
        try:
            roar = ""

            # Special Cases
            if length == "pi" or length == "🥧" or length == str(round(math.pi, len(length.split(".")[1]))):
                roar = random.choice(["R🥧O🥧A🥧R", "```\n  R\nR   O\n  A\n```"])
            elif int(length) == 69:
                roar = ':rolling_eyes:'
            elif int(length) == 666:
                roar = ':japanese_ogre:'
            elif int(length) <= 0:
                roar = 'How would I roar for zero or negative length!?'
            elif int(length) > 999:
                roar = 'I can\'t roar for that long!'

            # Normal Roar
            else:
                roar = 'R'
                for i in range(int(length)):
                    roar += 'o'
                for i in range(int(length)):
                    roar += 'a'
                roar += 'r'

            await ctx.send(roar)
        except TypeError:
            await ctx.send("I can\'t roar for an non integer length!")
