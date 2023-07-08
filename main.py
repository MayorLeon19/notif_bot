import asyncio
from discord_slash.utils.manage_commands import create_option
from discord_slash import SlashCommand
import discord
from discord.ext import commands
from discord_slash.model import ButtonStyle
import aiohttp
import time
from discord_components import DiscordComponents
from discord_slash.utils.manage_components import (
    create_button,
    create_actionrow
)
import discord
import os
# load our local env so we dont have the token in public
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from discord_components import DiscordComponents
import discord_components
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)  # Initialize the client class
TICKET_MOD_ROLE_ID = 1025824945374240768
MANAGEMENT_ROLE_ID = 947039787766906920
GUILD_ID = 924384808187093032
guild = bot.get_guild(GUILD_ID)
TICKET_CATEGORY_NAME = "Важное"
# Ignore these


# get the guild

# replace Active Tickets the exact name of your category (case sensitive)
@bot.event
async def on_message(message):
    if message.channel.id == 964626820270022766:
        if not message.content.startswith("<@&1060190025389707324>"):
            await message.add_reaction('💣')
            await message.author.send(embed = discord.Embed(description = f"""Привет! Пингуй пожалуйста @Объявления""", color = 0xe74c3c))
            time.sleep(5)
            await message.delete()
        elif message.content.startswith("<@&1060190025389707324>"):
          await message.add_reaction('<:socialdown_gl:1051890657171623997>')
          await message.add_reaction('<:socialup_gl:1051890655678431294>')
          await message.add_reaction('<:heart_gl:1052246668608819231>')
        else:
        	return
    elif message.channel.id == 964627157756284948:
        if not message.content.startswith("<@&1060189955315478589>"):
            await message.add_reaction('💣')
            await message.author.send(embed = discord.Embed(description = f"""Привет! Пингуй пожалуйста @Идея""", color = 0xe74c3c))
            time.sleep(5)
            await message.delete()
        elif message.content.startswith("<@&1060189955315478589>"):
            await message.add_reaction('🟥')
            await message.add_reaction('🟩>')
            await message.add_reaction('<:like:930499143229657099>')
        else:
            return
    elif message.channel.id == 964627209300103188:
        if not message.content.startswith("<@&947035477859508276>"):
            await message.add_reaction('💣')
            await message.author.send(embed = discord.Embed(description = f"""Привет! Пингуй пожалуйста @Авито""", color = 0xe74c3c))
            time.sleep(5)
            await message.delete()
        elif message.content.startswith("<@&947035477859508276>"):
            await message.add_reaction('🟩>')
            await message.add_reaction('🟥>')
        else:
            return
    elif message.channel.id == 954407985596203019:
        await message.add_reaction('🟥')
        await message.add_reaction('🟩')
        await message.add_reaction('<:like:930499143229657099>')

    else:
        return
@bot.event
async def on_ready():
    print(f"Авторизован как {bot.user}")
    DiscordComponents(bot)
@slash.subcommand(
    base="send",
    name="role",
    subcommand_group="shablon",
    guild_ids=[924384808187093032],
    description="отправить сообщение по роли",
    options=[
        create_option(
            name="role",
            description="роль",
            required=True,
            option_type=8,
        ),
        create_option(
            name="shablon",
            description="номер шаблона",
            required=True,
            option_type=10,
        ),
    ]
)

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(924384808187093032)
    message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
    if payload.message_id == 1025851431875510392:
        if payload.emoji.name == "🗒️":
            role = guild.get_role(930146424967032842)
            await payload.member.add_roles(role)
            await payload.member.send("Вам успешна выдана роль 'Объявления'!")
        elif payload.emoji.name == "🛒":
            role = guild.get_role(947035477859508276)
            await payload.member.add_roles(role)
            await payload.member.send("Вам успешна выдана роль 'Авито'!")
        elif payload.emoji.name == "📣":
            role = guild.get_role(945748731955937380)
            await payload.member.add_roles(role)
            await payload.member.send("Вам успешна выдана роль 'Идеи'!")
        else:
            print(f"'{payload.emoji}' : '{payload.emoji.name}'")
async def sendrole(ctx, role: discord.Role, shablon:str):
    guild = ctx.guild
    lol = shablon.isnumeric()
    if not lol:
        await ctx.author.send("Ошибка, msg не может быть числом")
    else:
        for member in guild.members:
            if role in member.roles:
                msg = int(msg)
                lol = sum(1 for line in open('setting_sendrole.ini'))
                if msg > lol:
                    await ctx.author.send("Ошибка, нет такой строки")
                else:
                    hah = msg - 1
                    a = open('setting_sendrole.ini').read().split('\n')[hah] % {'member': f'{member}', 'role': f'{role}', 'ctx.author': f'{ctx.author}', 'ctx.author.mention': f'{ctx.author.metion}', 'member.mention': f'{member.mention}', 'guild': f'{guild}', 'guild.members': f'{guild.members}', 'ctx.channel': f'{ctx.channel}', 'ctx.channel.mention': f'{ctx.channel.mention}', 'bot': f'{bot}', 'bot.user': f'{bot.user}', 'bot.user.mention': f'{bot.user.mention}'}
                    await member.send(f"{a}")
@slash.subcommand(
    base="send",
    name="role",
    subcommand_group="text",
    guild_ids=[924384808187093032],
    description="отправить сообщение по роли",
    options=[
        create_option(
            name="role",
            description="роль",
            required=True,
            option_type=8,
        ),
        create_option(
            name="text",
            description="сообщение",
            required=True,
            option_type=3,
        ),
    ]
)
async def sendtext(ctx, role:discord.Role, text:str):
    guild = ctx.guild
    for member in guild.members:
        if role in member.roles:
            text = text.replace(r"\n", "\n")
            await member.send(text)
# called whenever a button is pressed
@bot.event
async def on_button_click(interaction):
    ticket_created_embed = discord.Embed(
        title="Тикет создается",
        description=f"""Привет. Тикет открыт, тут ты можешь задать вопрос, не стесняйся! За фан тикет вы можете получить наказание.""",
    )
    guild = interaction.guild
    ticket_mod_role = guild.get_role(TICKET_MOD_ROLE_ID)
    ticket_category = guild.get_role(964617044316262400)
    management_role = guild.get_role(MANAGEMENT_ROLE_ID)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.user: discord.PermissionOverwrite(view_channel=True),
        guild.me: discord.PermissionOverwrite(view_channel=True),
        ticket_mod_role: discord.PermissionOverwrite(view_channel=False),
        management_role: discord.PermissionOverwrite(view_channel=True)
    }
    for channel in guild.channels:
        if channel.name == f"opened-ticket-{interaction.user.name}-{interaction.user.discriminator}":
            await interaction.send("Ошибка! У вас уже создан тикет!")

    ticket = await guild.create_text_channel(
        f"Opened-ticket-{interaction.user.name}-{interaction.user.discriminator}", overwrites=overwrites
    )

    await ticket.send(
        interaction.user.mention, embed=ticket_created_embed
    )  # ping the user who pressed the button, and send the embed

@slash.subcommand(
    base="ticket",
    name="send",
    guild_ids=[924384808187093032],
    description="отправить тикет")
@commands.has_role(TICKET_MOD_ROLE_ID)
async def send(ctx):
    embed = discord.Embed(
        title="Связь с администрацией",
        description="Нажмите на кнопку, чтобы открыть тикет",
    )

    actionrow = create_actionrow(
        *[
            create_button(
                label="Открыть тикет", custom_id="ticket", style=ButtonStyle.primary, emoji="🎫"
            ),
        ]
    )

    await ctx.send(embed=embed, components=[actionrow])

@slash.subcommand(
    base="ticket",
    name="approve",
    guild_ids=[924384808187093032],
    description="отправить сообщение по роли")
@commands.has_role(TICKET_MOD_ROLE_ID)
async def approve(ctx):
    ticket_mod_role = ctx.guild.get_role(TICKET_MOD_ROLE_ID)
    ticket_category = ctx.guild.get_role(964617044316262400)
    management_role = ctx.guild.get_role(MANAGEMENT_ROLE_ID)
    overwrites = {
        ctx.guild.me: discord.PermissionOverwrite(view_channel=True),
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
        management_role: discord.PermissionOverwrite(view_channel=False),
    }
    await ctx.channel.edit(overwrites=overwrites)

    await ctx.channel.send(
        "Тикет закрыт!\nВаш тикет был закрыт и перенесен для администрации. Они помогут вам в дальнейшем с вашим запросом."
    )

@slash.subcommand(
    base="ticket",
    name="close",
    guild_ids=[924384808187093032],
    description="закрыть тикет")
@commands.has_role(TICKET_MOD_ROLE_ID)
async def close(ctx):
    try:
        if int(ctx.channel.name[-4:]) > 0:
            chan = ctx.channel.name
            print(chan)
            chann = chan.replace("opened-ticket-", "closed-ticket-")
            print(chann)
            await ctx.channel.edit(name=chann)
        else:
            await ctx.author.send("❌ Это не тикет.")
    except:
        await ctx.author.send("❌ Это не тикет.")

@slash.subcommand(
    base="ticket",
    name="delete",
    guild_ids=[924384808187093032],
    description="удалить тикет")
@commands.has_role(TICKET_MOD_ROLE_ID)
async def delete(ctx):
    try:
        if int(ctx.channel.name[-4:]) > 0:
            await ctx.channel.delete()
        else:
            await ctx.author.send("❌ Это не тикет.")
    except:
        await ctx.author.send("❌ Это не тикет.")
@slash.subcommand(
    base="reaction",
    name="send",
    guild_ids=[924384808187093032],
    description="отправить сообщение с реакциями")
async def reactionsend(ctx):
    embed=discord.Embed(title="Получение роли 'Объявления'", description="Чтобы получить роль 'Объявления' нажмите 🗒️", color=0x61b356)
    embed2 = discord.Embed(title="Получение роли 'Идеи'", description="Чтобы получить роль 'Идеи' нажмите 📣",
                          color=0x61b356)
    embed3 = discord.Embed(title="Получение роли 'Авито'", description="Чтобы получить роль 'Авито' нажмите 🛒",
                          color=0x61b356)
    reaction = await ctx.channel.send(embeds=[embed,embed2,embed3])
    await reaction.add_reaction("🛒")
    await reaction.add_reaction("📣")
    await reaction.add_reaction("🗒️")

bot.run('')