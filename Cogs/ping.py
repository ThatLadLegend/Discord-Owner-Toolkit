from discord.ext import commands
import time


class PingCog(commands.Cog, name="ping command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
		
	@commands.command(
		name = "ping",
		usage=f"ping",
		description = "Display the bot's ping.",
		brief="Display the bot's ping.",
	)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def ping(self, ctx):
		before = time.monotonic()
		await ctx.typing()
		
		message = await ctx.send(f"🏓 Pong ! {self.bot.Bot.latency}")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"🏓 Pong !\nTime To Edit: {ping}`")

async def setup(bot:commands.Bot):
	await bot.add_cog(PingCog(bot))