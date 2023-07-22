import discord
from discord.ext import commands
from random import randint

class BotInfo(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(
		name = "Bot Info",
		usage="info",
		description = "Shows info about this bot.", 
		aliases=["info", "botinfo"],
		brief="Shows info about this bot."
	)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def info(self, ctx:commands.Context):
		embed=discord.Embed(title="Info For This Bot", description="Colour Generator is a bot that has 6 main features which include a `;cgen`, `;btc`, `;info`, `;ping`, `;help`, `;view`, and an `;invite` information grabber.\nMore commands may be added later down the line but for now that is it.", color=randint(500, 0xffffff))

		embed.add_field(name="Open Source GitHub Page", value="This bot is Open Sourced as I don't plan to add any too difficult commands.\n[Click here](https://github.com/LegendModzYT/Discord-Owner-Toolkit).", inline=False)

		embed.add_field(name="Invite This Bot", value=f"Invite Me Using This Link : [Click Here](https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=201403392).\n", inline=False)

		embed.set_footer(text=f"{ctx.message.author} - Discord Version {discord.__version__}", icon_url=ctx.message.author.avatar.url)
		await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
	await bot.add_cog(BotInfo(bot))