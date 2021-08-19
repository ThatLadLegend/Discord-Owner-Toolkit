import discord
from discord.ext import commands
import simplejson as json
from urllib.request import urlopen
import math
from random import randint

def get(url, object_hook=None):
    with urlopen(url) as resource:  # 'with' is important to close the resource after use
        return json.load(resource, object_hook=object_hook)


url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=GBP'

data = get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=GBP') # '{ "id": 1, "$key": 13213654 }'
ceiling = math.ceil(data['GBP'])


class btc(commands.Cog, name="Bitcoin Status"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(name = "btc", aliases=["bitcoin"], usage=";btc | ;bitcoin", description = "Shows the current BTC Price stats.")
	@commands.guild_only()
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def btc(self, ctx:commands.Context):
		await ctx.trigger_typing()
		embed=discord.Embed(title="Current BTC Price", description=f"\nBTC Price Now : __£{ceiling}__" ,color=randint(500, 0xffffff))
		embed.set_thumbnail(url="https://icons.iconarchive.com/icons/cjdowner/cryptocurrency-flat/1024/Bitcoin-BTC-icon.png")
		embed.timestamp = ctx.message.created_at
		embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(btc(bot))