import discord
from discord.ext import commands

TOKEN = 'NTYxNTk3MDA3MDg5NzYyMzEw.XJ-iMQ.LITM6VzaZPe9K6zxJ8kgRMIbSco'

bot = commands.Bot(command_prefix = 'csw!')

@bot.event
async def on_ready():
	print('Esta Vivooooo')
	
bot.run(TOKEN)
