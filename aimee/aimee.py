# This is a copy-paste from the Discord Red documentation on how to start this file, I have no clue on Python atm so naming will be screwed up
# Test comment

from redbot.core import commands

class AIMEE(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
