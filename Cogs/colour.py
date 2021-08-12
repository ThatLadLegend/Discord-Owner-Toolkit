import discord
from discord.ext import commands
from random import randint
import requests

b = randint(0, 0xffffff)
random_number = randint(1118481,16777215)
hex_number = str(hex(random_number))
dec_number = int(random_number)
hex_number ='#'+ hex_number[2:]


class cgen(commands.Cog, name="Colour Generator Command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "Cgen", aliases=["cgen"], usage=";cgen", description = "Generates Random Decimal Colours And Hex Code Colours, For Discord Roles And Embed Tool.")
	@commands.guild_only()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def cgen(self, ctx:commands.Context):
		embed = discord.Embed(title="Randomly Generated Colour.", description=f"Decimal Colour : {dec_number}\nHex Code : {hex_number}", color=randint(90, 0xffffff))
		await ctx.trigger_typing()
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(cgen(bot))
