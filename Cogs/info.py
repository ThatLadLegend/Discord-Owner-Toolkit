import discord
from discord.ext import commands

class UserInfo(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot


	@commands.command(name = "User Info", aliases = ["view", "userinfo"], usage = "<info mention>", brief="Grab User Info.", description = "A command which grabs the User Information of you or another member.")
	@commands.bot_has_permissions(send_messages=True)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def UserInfo(self, ctx:commands.Context, user: discord.Member = None):
		if (user is None):
			user = ctx.author
			
		await ctx.typing()
			
		embed = discord.Embed(title="User Info", description=f"User info for {user.mention}.", color=user.color)
		
		embed.add_field(name=f"Username", value=user, inline=True)
		embed.add_field(name=f"Activity", value=f"{user.activity if user.bot is False else 'Bot Status'}", inline=True)
		embed.add_field(name=f"User ID", value=user.id, inline=True)
		if (user.bot == True):
			embed.add_field(name=f"Is Bot", value=user.bot, inline=True)
			
		embed.add_field(name=f"Status", value=f"{'Do Not Disturb' if str(user.status).title() == 'Dnd' else str(user.status).title()}", inline=True)
		
		embed.add_field(name=f"Highest Role", value=user.top_role.mention, inline=True)

		embed.add_field(name = f"Account Created", value=f"<t:{int(user.created_at.timestamp())}:R>", inline=True)
		embed.add_field(name=f"Device", value=f"{'Mobile' if user.mobile_status != discord.Status.offline else ('Web' if user.web_status != discord.Status.offline else 'Desktop')}", inline=True)
		embed.add_field(name = f"Server Join Date", value=f"<t:{int(user.joined_at.timestamp())}:R>", inline=True)


		embed.set_thumbnail(url=user.avatar.url)
		embed.set_footer(text=f"Requested info by {ctx.message.author.global_name}.", icon_url=ctx.message.author.avatar.url)

		await ctx.reply(embed=embed)

class ServerInfo(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.has_permissions(manage_messages=True)
	@commands.command(name = "Server Info", aliases = ["serverinfo", "sinfo"], usage = f"sinfo", brief="Grab Server Info.", description = "A command which grabs the Server Information.")
	@commands.bot_has_permissions(send_messages=True)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def ServerInfo(self, ctx, server: discord.Guild = None):
		if (server is None):
			server = ctx.guild
			
		await ctx.typing()

		embed=discord.Embed(title="Server Info", description=f"## Server info for {server.name}.", color=ctx.message.author.color)

		embed.add_field(name=f"Server Owner", value=server.owner, inline=True)
		embed.add_field(name=f"Server Name", value=server.name, inline=True)
		embed.add_field(name=f"Members", value=f"{server.approximate_presence_count}/{len(server.members)}", inline=True)
		embed.add_field(name=f"Number Of Roles", value=len(server.roles), inline=True)


		# date_format = "%A, %d/%m/%Y"
		embed.add_field(name=f"Server Created", value=f"<t:{int(server.created_at.timestamp())}:R>", inline=False)

		embed.set_thumbnail(url=server.icon.url)
		embed.set_footer(text=f"Requested info by {ctx.message.author.global_name}.", icon_url=ctx.message.author.avatar.url)
		embed.timestamp = ctx.message.created_at

		await ctx.reply(embed=embed)


class InviteInfo(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(name = "Invite Info", aliases = ["invinfo", "inviteinfo", "invite"], usage = f"invite", brief="Grab Invite Info.", description = "A command which grabs the information of a valid Server invite..")
	@commands.bot_has_permissions(send_messages=True)
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def InviteInfo(self, ctx, invite: discord.Invite = None):
		if (invite is None):
			await ctx.reply("Please provide a valid invite.")
			return

		await ctx.typing()
		embed=discord.Embed(title="Invite Info", description=f"### Server Invite for [{invite.guild}]({invite.url}).", color=ctx.message.author.color)

		embed.add_field(name=f"Server Name", value=invite.guild, inline=True)

		embed.add_field(name=f"Invite ID", value=invite.id, inline=True)
		
		embed.add_field(name=f"Invite Channel", value=f"<#{invite.channel.id}>", inline=True)

		embed.add_field(name=f"Who Generated The Invite?", value=invite.inviter, inline=True)

		embed.add_field(name=f"Max Invite Age", value="Infinite" if invite.max_age == 0 else invite.max_age, inline=True)

		embed.add_field(name=f"Max Invite Uses", value="Infinite" if invite.max_uses == 0 else invite.max_uses, inline=True)

		embed.add_field(name=f"Approximate Member Count of Invited Server", value=f"{invite.approximate_presence_count}/{invite.approximate_member_count}", inline=True)

		embed.set_footer(text=f"Requested info by {ctx.message.author.global_name}.", icon_url=ctx.message.author.avatar.url)
		embed.timestamp = invite.created_at

		await ctx.reply(embed=embed)


async def setup(bot:commands.Bot):
	await bot.add_cog(UserInfo(bot))
	await bot.add_cog(ServerInfo(bot))
	await bot.add_cog(InviteInfo(bot))