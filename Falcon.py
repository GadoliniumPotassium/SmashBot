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
		tokens= message_content.split(" ")
		tokens= message_content.split(" ")
		tokens = list(filter(None, tokens))
		if(tokens == []):
			tokens=[1]
		if(tokens[0]=="!falcon"):
			if(len(tokens) == 1):
				await channel.send(RF.listCommands())
				return
			elif(tokens[1]=="help"):
				await channel.send(RF.listCommands())
			elif(tokens[1]=="rank"):
				await channel.send(RF.rankList([message.author.name])+"")
			elif(tokens[1]=="members"):
				await channel.send(RF.listLeagueMembers())
			elif(tokens[1]=="record"):
				await channel.send(RF.displayRecord([message.author.name]))
			elif(tokens[1]=="win" or tokens[1]=="loss"):
				await channel.send(RF.win_loss(message.author.id,tokens))
			elif (tokens[1]=="join"):
				await channel.send(RF.joinLeague([message.author.name,message.author.id]))
			elif (tokens[1]=="mac"):
				await channel.send("https://gph.is/1m04fun")
			elif (tokens[1]=="punch"):
				await channel.send("https://gfycat.com/violetperfumedindochinahogdeer")
			elif (tokens[1]=="RACIST" or tokens[1]=="racist"):
				file = discord.File("MachineRacist.png", filename="MachineRacist.png")
				await channel.send("I am indeed racist :)",file=file)
			else:
				await channel.send("This is not a valid command, try again or type :'!falcon help' for more information")

# start bot
client.run(TOKEN)
