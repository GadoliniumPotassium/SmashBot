#bot.py
import discord
import EventHandler
import ReactionFunctions
import SheetsController
from dotenv import load_dotenv
load_dotenv()
TOKEN = 'Njg3MzEwMjUwMjY0NDk0MTA1.Xmj7aw.rT9i1xA1O2raTdledApzfAOYtsU'
GUILD = '687313651216285811'
client = discord.Client()

EH=EventHandler

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
	message_content=message.content
	message_sender=message.author.name
	message_sender_id=message.author.id
	message_sender_id=message_sender_id
	print(str(message_content)+"\n"+str(message_sender)+"\n"+str(message_sender_id))
	#await message.content

# start bot
client.run(TOKEN)
