#bot.py
import discord
import EventHandler
import ReactionBoys
from dotenv import load_dotenv
load_dotenv()
TOKEN = 'Njg3MzEwMjUwMjY0NDk0MTA1.Xmj7aw.rT9i1xA1O2raTdledApzfAOYtsU'
GUILD = '687313651216285811'
client = discord.Client()

ch=EventHandler(client)

@client.event
async def on_ready():
	try:
		# print bot information
		print(client.user.name)
		print(client.user.id)
		print('Discord.py Version: {}'.format(discord.__version__))

	except Exception as e:
		print(e)

@client.event
async def on_message(message):
	# print message content
	await message.content

# start bot
client.run(TOKEN)
