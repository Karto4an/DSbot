import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix = '...') # , intents=discord.Intents.all()
slash = SlashCommand(bot)

async def remove_except(member, role):
    red = discord.utils.get(member.guild.roles, name = 'Red')
    green = discord.utils.get(member.guild.roles, name = 'Green')
    blue = discord.utils.get(member.guild.roles, name = 'Blue')
    yellow = discord.utils.get(member.guild.roles, name = 'Yellow')
    orange = discord.utils.get(member.guild.roles, name = 'Orange')
    purple = discord.utils.get(member.guild.roles, name = 'Purple')
    black = discord.utils.get(member.guild.roles, name = 'Black')
    white = discord.utils.get(member.guild.roles, name = 'White')
    role = role.name
    if role != 'Red':
        await member.remove_roles(red)
    if role != 'Green':
        await member.remove_roles(green)
    if role != 'Blue':
        await member.remove_roles(blue)
    if role != 'Yellow':
        await member.remove_roles(yellow)
    if role != 'Orange':
        await member.remove_roles(orange)
    if role != 'Purple':
        await member.remove_roles(purple)
    if role != 'Black':
        await member.remove_roles(black)
    if role != 'White':
        await member.remove_roles(white)

@slash.slash(name="red")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Red')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="green")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Green')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="blue")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Blue')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="yellow")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Yellow')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="orange")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Orange')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="purple")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Purple')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="black")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Black')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="white")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'White')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

bot.run('NTg4MDc2NjExMzI5NTg5MjU0.XP_3Bg.VbclgaU_VDjEVHy7rcF7Pak40-M')
