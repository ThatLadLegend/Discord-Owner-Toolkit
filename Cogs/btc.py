import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext import edit
import simplejson as json
from urllib.request import urlopen
import math

def get(url, object_hook=None):
    with urlopen(url) as resource:  # 'with' is important to close the resource after use
        return json.load(resource, object_hook=object_hook)


url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=GBP'

data = get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=GBP') # '{ "id": 1, "$key": 13213654 }'
ceiling = math.ceil(data['GBP'])

# print(json.dumps(data_json, indent=4, sort_keys=True))
# print(url.get('price'))


class btc(commands.Cog, name="Bitcoin Status"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	async def btc(self, ctx:commands.Context, msg_id: int = None, channel: discord.TextChannel = None):
		embed=discord.Embed(title="Current BTC Price", color=0xff0000)
		embed.add_field(name="BTC Price", value=f"\nBTC Status Now : __£{ceiling}__")
		embed.set_thumbnail(url="https://icons.iconarchive.com/icons/cjdowner/cryptocurrency-flat/1024/Bitcoin-BTC-icon.png")
		embed.timestamp = ctx.message.created_at
		embed.set_footer(text=ctx.message.author, icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(btc(bot))