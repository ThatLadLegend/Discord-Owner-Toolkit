import discord
from discord.ext import commands
from random import randint


class Info(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "info",
					usage=";info",
					description = "Shows info about this bot.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def info(self, ctx:commands.Context):
		embed=discord.Embed(title="Info For This Bot", description="Colour Generator is a bot that has two main features which include a `;cgen` and a `;btc`. More commands may be added later down the line but for tnow that is it.", color=randint(90, 0xffffff))
		embed.set_author(name="name", url="url", icon_url="icon")
		embed.set_thumbnail(url="thumbnail")
		embed.add_field(name="Open Source GitHub Page", value="This bot is Open Sourced as I don't plan to add any too difficult commands. [Click here](https://github.com/LegendModzYT/Colour-Gen-Bot)", inline=True)
		embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(Info(bot))