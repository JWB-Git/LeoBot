from discord.ext import commands
from constants import *
import math
import random
import json
import time
import discord


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
            if length == "pi" or length == "🥧" or \
                    ("." in length and length == str(round(math.pi, len(length.split(".")[1])))):
                roar = random.choice(["R🥧O🥧A🥧R", "```\n  R\nR   O\n  A\n```"])
            elif int(eval(length)) == 69:
                roar = ':rolling_eyes:'
            elif int(eval(length)) == 666:
                roar = ':japanese_ogre:'
            elif int(eval(length)) <= 0:
                roar = 'How would I roar for zero or negative length!?'
            elif int(eval(length)) > 999:
                roar = 'I can\'t roar for that long!'

            # Normal Roar
            else:
                roar = 'R'
                for i in range(int(eval(length))):
                    roar += 'o'
                for i in range(int(eval(length))):
                    roar += 'a'
                roar += 'r'

            await ctx.send(roar)
        except (TypeError, ValueError):
            await ctx.send("I can\'t roar for an non integer length!")


    @commands.command(name="catch", brief="Play catch with me", help="Let's play catch together")
    async def catch(self, ctx):
        if random.randint(0, 100) < 20:  # drops the ball occasionally
            options = [
                "Whoops, I missed the ball and the rest of my pride ripped it to shreds",
                "Whoops, as I went to pass it on the ball caught my claws and it deflated"
            ]
            await ctx.send(random.choice(options))
        else:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                catchers = data["catch"]
            if ctx.author.bot:
                print("Bot = True")
                await asyncio.sleep(random.randrange(2, 7))
            catcher = catchers[str(random.choice(range(len(catchers))))]
            timeout = time.time() + 10
            while time.time() < timeout:
                if int(catcher["id"]) in [member.id for member in ctx.guild.members if member.status == discord.Status.online] and not int(catcher["id"]) == 689981551534014576:
                    break
                catcher = catchers[str(random.choice(range(len(catchers))))]
            await ctx.send(f"{ctx.author.mention}, I whacked the ball with my paw over to <@{catcher['id']}> ...")
            if catcher.get("action") is not None:  # checks if bot requires an additional action to be able to catch
                await ctx.send(f"{catcher['action']}")
