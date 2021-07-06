import discord
from discord import guild
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dislash import SlashClient, ActionRow, Button, ButtonStyle
from discord_components import DiscordComponents, Button
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix = '...', intents=discord.Intents.all()) # , intents=discord.Intents.all()
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
    if payload.message_id == 861669668800692295:
        user = await bot.fetch_user(payload.user_id)
        reaction = str(payload.emoji)
        print(reaction)
        if reaction == "<:Dota2:861364008719613973>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            role = discord.utils.get(payload.member.guild.roles, name = '👺Пудж Сергей👺')
            await payload.member.add_roles(role)
            await check_role(payload.member)

        elif reaction == "<:CSGO:861941066847879198>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            role = discord.utils.get(payload.member.guild.roles, name = '🔫Каэсер')
            await payload.member.add_roles(role)
            await check_role(payload.member)

        elif reaction == "<:BrawlStars:861363718038093825>":
            guild = bot.get_guild(payload.guild_id)
            member = discord.utils.get(guild.members, id=payload.user_id)
            role = discord.utils.get(payload.member.guild.roles, name = '☠️Бравлер')
            await payload.member.add_roles(role)
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

async def check_role(member):
    role = discord.utils.get(member.guild.roles, name = '🌎𝙁𝙍𝙄𝙀𝙉𝘿')
    role_dev = discord.utils.get(member.guild.roles, name = 'Developer')
    if str(member.id) == '326784082501566475':
        await member.add_roles(role_dev)
    elif role not in member.roles:
        await member.add_roles(role)

@bot.command()
async def test(ctx):

    row_of_buttons = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Green button",
            custom_id="green"
        ),
        Button(
            style=ButtonStyle.red,
            label="Red button",
            custom_id="red"
        )
    )

    msg = await ctx.send(
        "This message has buttons!",
        components=[row_of_buttons]
    )

    def check(inter):
        return inter.message.id == msg.id
    inter = await ctx.wait_for_button_click(check)

    button_text = inter.clicked_button.label
    await inter.reply(f"Button: {button_text}")

bot.run(token)
