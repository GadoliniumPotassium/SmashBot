# bot.py
import discord
import ReactionFunctions
from random import randint
from os import listdir
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'Njg3MzEwMjUwMjY0NDk0MTA1.Xmj7aw.rT9i1xA1O2raTdledApzfAOYtsU'
GUILD = '686271323869151314'
client = discord.Client()

RF = ReactionFunctions

def handHolding():
    print ("Opening file")
    file = open("HandHolding.txt","r")
    gif = file.readlines()
    file.close()
    print ("Closing file")
    return gif[randint(0,len(gif)-1)]

def randomRacistReplies():
    print("Opening file")
    file = open("MR/racism.txt", "r")
    comments = file.readlines()
    print(comments)
    file.close()
    print("Closing file")
    return comments[randint(0, len(comments) - 1)]


def pullPictures(directory):
    pictures = listdir(directory)
    a = pictures[randint(0, len(pictures) - 1)]
    print(a)
    return a


def wholesomeReplies():
    print("Opening directories")
    return pullPictures("Wholesome")


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
        channel = message.channel
        # print message content
        message_content = message.content
        message_sender = message.author.name
        message_sender_id = message.author.id
        tokens = message_content.split(" ")
        tokens = message_content.split(" ")
        tokens = list(filter(None, tokens))
        if tokens == []:
            tokens = [1]
        if tokens[0] == "!falcon":
            if len(tokens) == 1:
                await channel.send(RF.listCommands())
                return
            elif tokens[1] == "help":
                await channel.send(RF.listCommands())
            elif tokens[1] == "rank":
                await channel.send(RF.rankList([message.author.name]) + "")
            elif tokens[1] == "members":
                await channel.send(RF.listLeagueMembers())
            elif tokens[1] == "record":
                await channel.send(RF.displayRecord([message.author.name]))
            elif tokens[1] == "win" or tokens[1] == "loss":
                await channel.send(RF.winOrLoss(message.author.id, tokens))
            elif tokens[1] == "join":
                print('running join league')
                await channel.send(RF.joinLeague([message.author.name, message.author.id]))
            elif tokens[1] == "mac":
                print('falcon mac')
                await channel.send("https://66.media.tumblr.com/20de21ba3c860193d7c934543634eb03"
                                   "/tumblr_n0ygmlpXPh1s8ouhxo1_500.gif")
            elif tokens[1] == "punch":
                print('running falcon punch')
                await channel.send("https://gfycat.com/violetperfumedindochinahogdeer")
            elif tokens[1] == "RACIST" or tokens[1] == "racist":
                print('gonna print racism')
                pic = pullPictures("MR/Pictures/")
                file = discord.File("MR/Pictures/" + pic, filename=pic)
                await channel.send(randomRacistReplies(), file=file)
            elif tokens[1] == "WHOLESOME" or tokens[1] == "wholesome" or tokens[1] == "love" or tokens[1] == "cute":
                print('gonna print wholesome pic')
                pic = wholesomeReplies()
                file1 = discord.File("Wholesome/" + pic, filename=pic)
                await channel.send("Heres a bit of wholesome, love you <3", file=file1)
            elif tokens[1] == "GG" or tokens[1] == "gg":
                print("running gg")
                await channel.send("Thank you for having fun playing a good game of smash!")
            elif tokens[1] == "thank" and tokens[2] == "you":
                print("thank you command")
                await channel.send("You're welcome " + message_sender + " :heart:")
            elif tokens[1] == "challenge":
                person = tokens[2]
                await channel.send(message_sender + " has challenged " + person)
            elif tokens[1] == "funny" or tokens[1] == "haha":
                await channel.send(RF.returnFunnyLink())
            elif tokens[1]=="lewd":
                await channel.send(handHolding())
            else:
                await channel.send(
                    "This is not a valid command, try again or type :'!falcon help' for more information")


# start bot
client.run(TOKEN)
