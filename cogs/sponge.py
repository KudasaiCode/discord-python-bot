import discord
from discord.ext import commands

class Sponge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 188112415110463488:
            await message.channel.send('https://cdn.discordapp.com/attachments/308319657499295744/628107829324283920/2ohl2d.jpg')
        else:
            pass

def setup(client):
    client.add_cog(Sponge(client))
