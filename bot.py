import discord
from discord import guild
from discord.ext import commands, tasks
from discord_slash import SlashCommand, SlashContext
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

intents = discord.Intents().all()

bot = commands.Bot(command_prefix = '...', intents=intents) # , intents=discord.Intents.all()
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
    indigo = discord.utils.get(member.guild.roles, name = 'Indigo')
    pink = discord.utils.get(member.guild.roles, name = 'Pink')
    coral = discord.utils.get(member.guild.roles, name = 'Coral')
    drkgrn = discord.utils.get(member.guild.roles, name = 'Dark green')
    rnbw = discord.utils.get(member.guild.roles, name = 'Antinatural')

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
    if role != 'Antinatural':
        await member.remove_roles(rnbw)

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

@slash.slash(name="rainbow")
async def _test(ctx: SlashContext):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name = 'Antinatural')
    await member.add_roles(role)
    message = await ctx.send('Success!')
    await ctx.message.delete()
    await remove_except(member, role)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 862474653385883668:
        user = await bot.fetch_user(payload.user_id)
        reaction = str(payload.emoji)
        print(reaction)
        
        role3 = discord.utils.get(payload.member.guild.roles, name = '☠️𝐁𝐫𝐚𝐰𝐥 𝐒𝐭𝐚𝐫𝐬') 
        role1 = discord.utils.get(payload.member.guild.roles, name = '👺𝐃𝐎𝐓𝐀')
        role2 = discord.utils.get(payload.member.guild.roles, name = '🔫𝐂𝐒𝐆𝐎')
        
        if reaction == "<:Dota2:861364008719613973>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            await payload.member.add_roles(role1)
            await check_role(payload.member)

        elif reaction == "<:CSGO:861941066847879198>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            await payload.member.add_roles(role2)
            await check_role(payload.member)

        elif reaction == "<:BrawlStars:861363718038093825>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            await payload.member.add_roles(role3)
            await check_role(payload.member)
        elif reaction == "❌":
            guild = bot.get_guild(payload.guild_id)
            member = bot.get_user(payload.user_id)
            channel = bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            await message.remove_reaction('❌', member)
            await message.remove_reaction('<:Dota2:861364008719613973>', member)
            await message.remove_reaction('<:CSGO:861941066847879198>', member)
            await message.remove_reaction('<:BrawlStars:861363718038093825>', member)
            
            await payload.member.remove_roles(role3)
            await payload.member.remove_roles(role2)
            await payload.member.remove_roles(role1)

async def check_role(member):
    role = discord.utils.get(member.guild.roles, name = '🌎𝙁𝙍𝙄𝙀𝙉𝘿')
    role_dev = discord.utils.get(member.guild.roles, name = 'Developer')
    if str(member.id) == '326784082501566475':
        await member.add_roles(role_dev)
    elif role not in member.roles:
        await member.add_roles(role)
        
@tasks.loop(minutes=5, count=None, reconnect=True, loop=None)
async def change_status():
    await bot.wait_until_ready()
    guild = bot.get_guild(576409704155316234)

    channel = bot.get_channel(862744855171039243)
    print(channel)
    member_count = len([m for m in guild.members if not m.bot])
    print(member_count)
    await channel.edit(name=f"All members: {member_count}")

change_status.start()
bot.run(token)
