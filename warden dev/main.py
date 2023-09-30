import discord
from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    async def on_ready(self):
        print('Bot is ready!')

bot = MyBot()
bot.run('MTE1Nzc4Nzc5OTkyNDI0NDUxMA.G7Bfo-.pTXvqvcs5Hj3BSVWQjl2VsISpwkfT59tpnp0tU')