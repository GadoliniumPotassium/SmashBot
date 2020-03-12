#bot.py
import discord
import ReactionFunctions
import SheetsController
from dotenv import load_dotenv
load_dotenv()
TOKEN = 'Njg3MzEwMjUwMjY0NDk0MTA1.Xmj7aw.rT9i1xA1O2raTdledApzfAOYtsU'
GUILD = '686271323869151314'
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
		print(message.content)
		print(message_sender_id)
		tokens= message_content.split(" ")
		tokens= message_content.split(" ")
		tokens = list(filter(None, tokens))
		print(tokens)
		if(tokens[0]=="!falcon"):
			if(len(tokens) == 1):
				await channel.send(RF.listCommands())
				return
			elif(tokens[1]=="help"):
				print(RF.listCommands())
				await channel.send(RF.listCommands())
			elif(tokens[1]=="rank"):
				print(RF.rankList([message.author.name,""]))
				await channel.send(RF.rankList([message.author.name])+"")
			elif(tokens[1]=="members"):
				print(RF.listLeagueMembers())
				await channel.send(RF.listLeagueMembers())
			elif(tokens[1]=="record"):
				print(RF.displayRecord([message.author.name]))
				await channel.send(RF.displayRecord([message.author.name]))
			elif(tokens[1]=="win" or tokens[1]=="loss"):
				await channel.send(RF.win_loss(message.author.id,tokens))
			elif (tokens[1]=="join"):
				await channel.send(RF.joinLeague([message.author.name,message.author.id]))
			elif (tokens[1]=="mac"):
				await channel.send("https://gph.is/1m04fun")
			elif (tokens[1]=="punch"):
				await channel.send("https://gfycat.com/violetperfumedindochinahogdeer")

			else:
				await channel.send("This is not a valid command, try again or type :'!falcon help' for more information")

			


# start bot
client.run(TOKEN)
