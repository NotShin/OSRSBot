import discord
import asyncio
import sys, traceback
from discord.ext import commands
from commands.ext.utils import GetGiveawayStatus, AddEntrant

description        = '''Giveaway bot for the Old School RuneScape Discord.'''
startup_extensions = ["commands.oldschool"]

bot = commands.Bot(command_prefix="!", description=description, pm_help=True)

@bot.event
async def on_ready():
    print ('Logged in as')
    print (bot.user.name)
    print (bot.user.id)
    print ('------')

@bot.command(hidden=True, no_pm=True, pass_context=True)
async def load(ctx, extension_name : str):
	"""Loads an extension."""
	if str(ctx.message.author.top_role) == "Admin":
		try:
			bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await bot.say("{} loaded.".format(extension_name))
	else:
		await bot.send_message(message.author, "You are not authorized to use that command.")

@bot.command(hidden=True, no_pm=True, pass_context=True)
async def unload(ctx, extension_name : str):
	"""Unloads an extension."""
	if str(ctx.message.author.top_role) == "Admin":
		bot.unload_extension(extension_name)
		await bot.say("{} unloaded.".format(extension_name))
	else:
		await bot.send_message(message.author, "You are not authorized to use that command.")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.startswith("!") and str(message.author.top_role) == "Admin":
		await bot.process_commands(message)
	if await GetGiveawayStatus():
		if str(message.author.top_role) != "Admin":
			await AddEntrant(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run('token')
