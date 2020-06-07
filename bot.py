import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '/tut ')

@client.event
async def on_ready():
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
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

client.run('NzE5MjYzMzI3ODYzNDM5Mzgz.Xt04Og.HKiKU72Cr0UMxis-H3Q9RglVABc')