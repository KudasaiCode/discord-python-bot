import discord
from discord.ext import commands

'''
Simple command that returns the
requested user's avatar in a larger size.
'''

class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avi(self, ctx, member: discord.Member):
        await ctx.send(member.avatar_url)

    @avi.error
    async def avi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('> Who\'s avi?')

def setup(client):
    client.add_cog(User(client))
