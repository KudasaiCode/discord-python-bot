import discord
from discord.ext import commands
import random
from random import *

'''
Small simple commands that execute basic fun.
# d20: rolls a d20
# dice: rolls one die
# ping: checks your ping in ms
# coin: Flips a coin
# 8ball: have a ball give you your fortune
'''
class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def d20(self, ctx):
    	roll = randint(1, 20)
    	await ctx.send(f'> {roll}')

    @commands.command()
    async def dice(self, ctx):
    	roll = randint(1, 6)
    	await ctx.send(f'> {roll}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"> Your ping is: {bot.latency * 1000}ms")

    @commands.command()
    async def coin(self, ctx):
        flip = ['Heads', 'Tails']
        await ctx.send(f'> {choice(flip)}')

    @commands.command(aliases=['8b','8ball'])
    async def _8ball(self, ctx, *, question):
    	responses = ['It is cerain.',
    				'It is decidedly so.',
    				'Without a doubt',
    				'Yes, definitely.',
    				'You may rely on it.',
    				'As i see it, yes.',
    				'Most likely.',
    				'The outlook is good.',
    				'Maybe.',
    				'Lol nah',
    				'Try again.',
    				'No.',
    				'Definitely not.',
    				'My sources say no.',
    				'Doubtful.',
    				'Perhaps.',
    				'I don\'t like your attitude.',
    				'Not really.']

    	if question[-1] != '?':
    		doubt = ['Did you forget how to use punctuation marks again?',
    				 'That is not a question.']
    		await ctx.send(f'> {choice(doubt)}')
    	else:
    		await ctx.send(f'> {choice(responses)}')

def setup(client):
    client.add_cog(Fun(client))
