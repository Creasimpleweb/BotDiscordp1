import discord
from discord.ext import commands

TOKEN = 'tu token'

bot = commands.Bot(command_prefix = 'csw!')

@bot.event
async def on_ready():
	print('Esta Vivooooo')
	
bot.run(TOKEN)
