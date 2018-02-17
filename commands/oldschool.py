import discord
import asyncio
from discord.ext import commands
from commands.ext.utils import SetGiveawayOn, SetGiveawayOff, GameMessage, ChooseWinner, ClearEntrants

class Oldschool():
	def __init__(self, OSRSBot):
		self.OSRSBot  = OSRSBot
		self.giveaway = None

	@commands.command(name="setgiveaway", no_pm=True, pass_context=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def set(self, ctx, text : str):
		""" Sets the giveaway text. """
		self.giveaway = ' '.join(ctx.message.content.split(' ')[1:])
		await self.OSRSBot.send_message(ctx.message.channel, "{} Giveaway message set.".format(ctx.message.author.mention))
		return

	@commands.command(name="startgiveaway", no_pm=True, pass_context=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def start(self, ctx):
		""" Starts a giveaway. """
		await GameMessage(self.OSRSBot, ctx.message, "Giveaway", self.giveaway)
		await SetGiveawayOn()
		return

	@commands.command(name="endgiveaway", no_pm=True, pass_context=True)
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def end(self, ctx):
		""" Ends a giveaway. """
		winner = await ChooseWinner()
		if winner != -1:
			await GameMessage(self.OSRSBot, ctx.message, "Giveaway", "Congratulations {}! You won the giveaway!".format(winner))
		else:
			await GameMessage(self.OSRSBot, ctx.message, "Giveaway", "No winner was chosen as nobody entered the giveaway.")
		await SetGiveawayOff()
		await ClearEntrants()
		return

def setup(OSRSBot):
	OSRSBot.add_cog(Oldschool(OSRSBot))