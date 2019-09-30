import discord
from discord.ext import commands
import random
import typing
import os
import nacl
import json

# server specific prefix fetch
def get_prefix(client, message):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]

# Apply prefix to server
bot = commands.Bot(command_prefix = get_prefix)

# initial check
@bot.event
async def on_ready():
	print("I am working beep boop.")

	# Change status
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('Smoking Weed'))

# incorrect command error
@bot.event
async def on_command_error(ctx, error):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)
		prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f'> Invalid command used.\n> use {prefix}help to see command list.')

@bot.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@bot.event
async def on_member_remove(member):
	print(f'{member} has left the server')

# bulk delete messages
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
	amount += 1
	await ctx.channel.purge(limit=amount)
# command specific error handling
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('You do not have permission to use this command.')

# Manipulates prefixes.json #
############################
# joining guild default prefix
@bot.event
async def on_guild_join(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '/'

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

# leaving guild remove prefix from json
@bot.event
async def on_guild_remove(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

# change prefix and update json
@bot.command(aliases=['changeprefix'])
@commands.has_permissions(administrator=True)
async def change_prefix(ctx, prefix):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(ctx.guild.id)] = prefix

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

	await ctx.send(f'> updated prefix to: {prefix}')

# cogs section #
################
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')

# loads all cogs found in './cogs'
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

print('Cogs loaded')

bot.run('NjI3MTAxNjQwNDQ0MzQ2Mzcw.XY3wPw.rsWgShDD0aR6bZT4FU2gfq7Yvz4')
