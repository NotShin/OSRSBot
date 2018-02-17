import math
import discord
from random import SystemRandom

_sysrand = SystemRandom()
status   = False
entrants = []

#This is a secure dice roll function that produces a random number between 1 and outof
async def RollDice(outof):
	if (outof < 2):
	    return 0
	global _sysrand
	return math.floor(_sysrand.random() * outof) + 1

async def GameMessage(bot, message, title_of_embed, message_to_send):
	em = discord.Embed(title=title_of_embed, description=message_to_send, colour=discord.Color.blue(), url='https://www.sythe.org/')
	em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
	em.set_thumbnail(url='https://files.coinmarketcap.com/static/img/coins/64x64/rsgpcoin.png')
	await bot.send_message(message.channel, embed=em)
	return

async def SetGiveawayOn():
	global status
	status = True
	return

async def SetGiveawayOff():
	global status
	status = False
	return

async def GetGiveawayStatus():
	return status

async def AddEntrant(message):
	global entrants
	if message.author.mention not in entrants:
		entrants.append(message.author.mention)
	return

async def ChooseWinner():
	global entrants
	try:
		result = await RollDice(len(entrants)) - 1
		return entrants[result]
	except:
		return -1

async def ClearEntrants():
	global entrants
	entrants.clear()
	return