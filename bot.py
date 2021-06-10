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
    silver = discord.utils.get(member.guild.roles, name = 'Silver')
    #new
    indigo = discord.utils.get(member.guild.roles, name = 'Indigo')
    pink = discord.utils.get(member.guild.roles, name = 'Pink')
    coral = discord.utils.get(member.guild.roles, name = 'Coral')
    drkgrn = discord.utils.get(member.guild.roles, name = 'Dark green')

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
    if role != 'Silver':
        await member.remove_roles(silver)
    #new
    if role != 'Indigo':
        await member.remove_roles(indigo)
    if role != 'Pink':
        await member.remove_roles(pink)
    if role != 'Coral':
        await member.remove_roles(coral)
    if role != 'Dark green':
        await member.remove_roles(drkgrn)

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

@slash.slash(name="silver")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Silver')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)


#new


@slash.slash(name="coral")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Coral')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="pink")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Pink')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="dark_blue")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Indigo')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@slash.slash(name="dark_green")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Dark green')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='🌎𝙁𝙍𝙄𝙀𝙉𝘿')
    await member.add_roles(role)
    if (member.id == 326784082501566475):
        developer = discord.utils.get(member.guild.roles, name='Developer')
        await member.add_roles(developer)

bot.run('NTg4MDc2NjExMzI5NTg5MjU0.XP_3Bg.VbclgaU_VDjEVHy7rcF7Pak40-M')
