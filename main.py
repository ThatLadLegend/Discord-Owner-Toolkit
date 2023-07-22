import json
import os

import asyncio

from random import randint

import discord
from discord.ext import commands


# Get config.json
with open("config.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]

# Intents
intents = discord.Intents.all()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

@bot.event
async def on_ready():
	guilds = len(bot.guilds)
	if (guilds > 1):
		print(f"\nBot Name: {bot.user}\nBot ID: {bot.user.id}\nBot Token: {token}\nThe Bot Is In {guilds} Servers.")
	else:
		print(f"\nBot Name: {bot.user}\nBot ID: {bot.user.id}\nBot Token: {token}\nThe Bot Is In {guilds} Server.")
	print(f"\n\nInvite Me Using This Link : https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=201403392.\n")
	print(f"Current Discord Version : {discord.__version__}.")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"for {bot.command_prefix}help"))

async def loadCogs():
	for filename in os.listdir("./Cogs"):
		if filename.endswith(".py"):
			await bot.load_extension(f"Cogs.{filename[:-3]}")
			print(f"Cogs.{filename[:-3]}")


@bot.command(name = "Reload Cogs", aliases = ["reload"], usage = f"reload", description = "A command to reload specific or all currently loaded cogs.", hidden=True)
@commands.is_owner()
async def ReloadCogs(ctx, cogs: str = None):
	if cogs is None:
		for filename in os.listdir("./Cogs"):
			if filename.endswith(".py"):
				await bot.reload_extension(f"Cogs.{filename[:-3]}")
		await ctx.reply("Reloaded all cogs.")
	else:
		try:
			await bot.reload_extension(f"Cogs.{cogs}")
			await ctx.reply(f"Reloaded {cogs} cog.")
		except commands.ExtensionNotFound:
			await ctx.reply(f"Cog {cogs} not found.")
				
		except commands.NotOwner:
			await ctx.reply(f"No lmao, stupid.")


async def main():
	await loadCogs()
	await bot.start(token)

asyncio.run(main())