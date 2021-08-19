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


	@commands.command(name = "Colour Generator", aliases=["cgen"], usage=";cgen", description = "Generates Random Decimal Colours And Hex Code Colours, For Discord Roles And Embed Tool.")
	@commands.guild_only()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def cgen(self, ctx:commands.Context):
		await ctx.trigger_typing()
		embed = discord.Embed(title="Randomly Generated Colour.", description=f"Decimal Colour : {dec_number}\nHex Code : {hex_number}", color=randint(500, 0xffffff)) # Doesn't really work so I change.
		embed.timestamp = ctx.message.created_at
		embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(cgen(bot))
