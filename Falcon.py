#bot.py
import discord
import ReactionFunctions
import SheetsController
from dotenv import load_dotenv
load_dotenv()
TOKEN = 'Njg3MzEwMjUwMjY0NDk0MTA1.Xmj7aw.rT9i1xA1O2raTdledApzfAOYtsU'
GUILD = '687313651216285811'
client = discord.Client()

RF=ReactionFunctions

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
	if message.author == client.user:
		pass
	else:
		channel=message.channel
		# print message content
		message_content=message.content
		message_sender=message.author.name
		message_sender_id=message.author.id
		message_sender_id=message_sender_id
		tokens= message_content.split(" ")
		tokens = list(filter(None, tokens))
		if(tokens[0]=="!falcon" and len(tokens)>1):
			if(tokens[1]=="help"):
				print(RF.listCommands())
				await channel.send(RF.listCommands())
			elif(tokens[1]=="rank"):
				print(RF.rankList())
				await channel.send(RF.rankList())
			elif(tokens[1]=="members"):
				print(RF.listLeagueMembers())
				await channel.send(RF.listLeagueMembers())
			elif(tokens[1]=="record"):
				print(RF.displayRecord([message.author.name]))
				await channel.send(RF.displayRecord([message.author.name]))
			elif(tokens[1]=="win" or tokens[1]=="loss"):
				await channel.send(RF.win_loss(tokens, message.author.name))
			elif (tokens[1]=="join"):
				await channel.send(RF.joinLeague([message.author.name,message.author.id]))
		else:
			await channel.send("This is not a valid command, try again or type :'!falcon help' for more information")
			


# start bot
client.run(TOKEN)
