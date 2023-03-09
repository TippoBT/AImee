# This is a copy-paste from the Discord Red documentation on how to start this file, I have no clue on Python atm so naming will be screwed up
# Test comment

from redbot.core import commands

class AIMEE(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def AIsay(ctx, *, text):
        #Should repeat voicename and the message
        ## wait self.bot(text)
        await ctx.send(text)
