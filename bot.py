import discord
from discord.ext import commands, tasks
import random
from itertools import cycle

client = commands.Bot(command_prefix = '/tut ')
status = cycle(['Status 1','Status 2'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(aliases = ['8ball','test'])
async def _8ball(ctx,*,question):
    responses = ['Yes','No','Maybe']
    await ctx.send(f'Question:{question} \n Answer:{random.choice(responses)}')

@client.command()
async def kick(ctx,member : discord.Member,*,reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount : int):
    await ctx.channel.purge(limit=amount)

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

def is_it_me(ctx):
    return ctx.author.id == 558031036358066204

@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f"Hi it's me {ctx.author}")

###Error Handling####

@client.event
async def on_command_error(ctx,error):
    if(isinstance(error,commands.CommandNotFound)):
        await ctx.send("Invalid Command")

@clear.error
async def clear_error(ctx,error):
    if(isinstance(error,commands.MissingRequiredArgument)):
        await ctx.send("Please specify amount of messages to delete")

client.run('RANDOMKEY')