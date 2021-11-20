
#############################################################################
#                                                                           #                                          #                                                                   #                                                                          #
# Response Bot Discord.py                                                   #
# Made by rhysfr on Github!                                                 #
#                                                                           #
#############################################################################


import discord # importing discord module

bot = discord.Client() 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Your Status Here')) # Change your status here
    print('Connected to bot: {}'.format(bot.user.name)) # Shows that bot is connected to your token and Discord API
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'Hello!' in message.content:
        await message.channel.send('Hello there!')  # Add your responses here. 

bot.run('Token Here.')  # Put your token here
