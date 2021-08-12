import discord
from discord.ext import commands
import json
import os

# Get config.json
with open("config.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

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

bot.run(token)