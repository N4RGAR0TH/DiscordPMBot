import discord
from datetime import datetime
from discord import guild, Intents, member
from discord.ext import commands
from asyncio import sleep
intents = discord.Intents().all()
client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready():
    print("Bot ready")

#Inform when get message
@client.event
async def on_message(message):
    if message.guild is None and message.author != client.user:
        dateTimeObj = datetime.now()
        print(str(dateTimeObj) + " \033[92m(DM)" + str(message.author) + ": " + message.content + "\033[0m")
    await client.process_commands(message)

#Print the pm details
@client.command()
async def pm(ctx, victim: discord.Member, amount, *, message):
    for _ in range(int(amount)):
        await victim.send(message)
        dateTimeObj = datetime.now()
        print (str(dateTimeObj) + " \033[94mBot to " + str(victim) + ": " + message + "\033[0m")

#Pms everyone in a server
@client.command()
async def pmall(ctx, *, message):
    guild = ctx.guild
    for m in guild.members:
        try:
            await m.send(message)
            print(f" DM sent to {m}.")
        except Exception as e:
            print(f"Couldn't message {m}\n\n\n{e} , probably have their PM's disabled against non-friends")

    await ctx.send(f"All members messaged")

client.run("token-here")