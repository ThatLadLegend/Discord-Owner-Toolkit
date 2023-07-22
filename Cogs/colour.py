import discord
from discord.ext import commands
from random import randint
import requests

b = randint(0, 0xffffff)
random_number = randint(1118481,16777215)
hex_number = str(hex(random_number))
dec_number = int(random_number)
hex_number ='#'+ hex_number[2:]


class cgen(commands.Cog, name="Colour Generator"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(
			name = "cgen",
			usage="cgen",
			brief="Generate Random Colour.",
			description = "Generates random decimal colours and hex code colours, for Discord roles and embed tool."
	)
	@commands.guild_only()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def cgen(self, ctx:commands.Context):
		await ctx.typing()
		embed = discord.Embed(title="Randomly Generated Colour.", description=f"Decimal Colour : {dec_number}\nHex Code : {hex_number}", color=randint(500, 0xffffff)) # Doesn't really work so I change.
		embed.timestamp = ctx.message.created_at
		embed.set_footer(text=ctx.message.author.global_name, icon_url=ctx.message.author.avatar.url)
		await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
	await bot.add_cog(cgen(bot))
