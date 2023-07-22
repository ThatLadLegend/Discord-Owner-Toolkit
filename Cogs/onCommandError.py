from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner

class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				await ctx.reply('This command has a cooldown, for '+str(day)+ "day(s)")
			elif hour > 0:
				await ctx.reply('This command has a cooldown, for '+str(hour)+ " hour(s)")
			elif minute > 0:
				await ctx.reply('This command has a cooldown, for '+ str(minute)+" minute(s)")
			else:
				await ctx.reply(f'This command has a cooldown, for {error.retry_after:.2f} second(s)')
		elif isinstance(error, CommandNotFound):
			return
		elif isinstance(error, MissingPermissions):
			await ctx.reply(error)
		elif isinstance(error, CheckFailure):
			await ctx.reply(error)
		elif isinstance(error, NotOwner):
			await ctx.reply(error)
		else:
			await ctx.reply(error)

async def setup(bot):
	await bot.add_cog(OnCommandErrorCog(bot))
