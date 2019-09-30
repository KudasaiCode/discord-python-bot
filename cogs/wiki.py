import discord
from discord.ext import commands
import wikipedia

'''
uses wikipedia's api
to fetch a summary of
a key word/s
'''
class Wiki(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def wiki(self, ctx, *, search):
		summary = wikipedia.summary(search, sentences = 3)
		await ctx.send("> " + summary)

def setup(client):
    client.add_cog(Wiki(client))
