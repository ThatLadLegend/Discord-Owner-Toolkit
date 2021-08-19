import discord
from discord.ext import commands
from random import randint


class UserInfo(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "User Info", aliases = ["view", "userinfo"], usage = "<info mention>", description = "A command which grabs the User Information of you or another member.")
	@commands.bot_has_permissions(send_messages=True)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def UserInfo(self, ctx:commands.Context, user: discord.Member = None):
		if (user == None):
			user = ctx.author

		embed=discord.Embed(title="User Info", description=f"User info for {user.mention}", color=randint(500, 0xffffff))
		embed.add_field(name=f"Username", value=f"{user.name}", inline=True)
		embed.add_field(name=f"User ID", value=f"{user.id}", inline=True)

		role = ctx.author.roles
		role.reverse()
		highest_role = role[0]
		embed.add_field(name=f"Highest Role", value=f"{highest_role}", inline=True)

		date_format = "%a, %d/%b/%Y"
		embed.add_field(name=f"Created", value=f"{user.created_at.strftime(date_format)}", inline=False)
		embed.add_field(name=f"Server Join Date", value=f"{user.joined_at.strftime(date_format)}", inline=True)


		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		embed.set_footer(text=f"Requested info by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)


def setup(bot:commands.Bot):
	bot.add_cog(UserInfo(bot))