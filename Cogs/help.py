import discord
from discord.ext import commands
from random import randint

class HelpCog(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(
		name = 'Help',
		usage=f"help",
		description = "Display the help embed or shows help for a specfic command.",
		aliases = ["h", "help"],
		brief = "Display the help embed.",
	)
	
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def help (self, ctx, commandName:str=None):

		commandName2 = None
		stop = False
		await ctx.typing()

		if commandName is not None:
			for i in self.bot.commands:
				if i.name == commandName.lower():
					commandName2 = i
					break 
				else:
					for j in i.aliases:
						if j == commandName.lower():
							commandName2 = i
							stop = True
							break
						if stop is True:
							break 

			if commandName2 is None:
				await ctx.channel.send("No command found!")   
			else:
				embed = discord.Embed(title=f"{commandName2.cog_name.title()} Command", description="", color=randint(500, 0xffffff))

				embed.set_thumbnail(url=f'{ctx.message.author.avatar.url}')
				embed.add_field(name=f"Name", value=f"{commandName2.name}", inline=True)
				aliases = commandName2.aliases
				aliasList = ""
				if len(aliases) > 0:
					for alias in aliases:
						aliasList += alias + " | "
					aliasList = aliasList[:-2]
					embed.add_field(name=f"Aliases", value=aliasList)
				else:
					embed.add_field(name=f"Aliases", value="None", inline=True)

				if commandName2.usage is None:
					embed.add_field(name=f"Usage", value=f"None", inline=True)
				else:
					embed.add_field(name=f"Usage", value=f"{commandName2.usage}", inline=True)
				embed.add_field(name=f"Description", value=f"{commandName2.description}", inline=True)
				embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar.url)
				await ctx.message.reply(embed=embed)			 
		else:
			embed = discord.Embed(title=f"Help Page", color=randint(500, 0xffffff))
			embed.set_thumbnail(url=f'{self.bot.user.avatar.url}')
			for i in self.bot.commands:
				if not i.hidden:
					embed.add_field(name=i.name.title(), value=i.brief, inline=True)

				elif ctx.message.author.id == self.bot.owner_id:
					embed.add_field(name=i.name.title(), value=i.brief, inline=True)

				else:
					pass

			embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar.url)
			await ctx.message.reply(embed=embed)

async def setup(bot:commands.Bot):
	bot.remove_command("help")
	await bot.add_cog(HelpCog(bot))
