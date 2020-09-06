import discord
from discord.ext import commands
import asyncio
import requests
import random as r
import sqlite3
import os


client = commands.Bot(command_prefix='/')


@client.event
async def on_ready(*args):
    print ( 'Бот Подключён!Можно работать.' )
    type = discord.ActivityType.watching
    activity = discord.Activity(name = "на маму Ярика)00", type = type)
    status = discord.Status.dnd
    await client.change_presence(activity = activity, status = status)



@client.event
async def on_member_join( member ):
    emb = discord.Embed( description = f"**<:3772_TsukimiyaSip:730480801011204216> Пользователь **{member.mention}**, присоединился к серверу!<:3772_TsukimiyaSip:730480801011204216> **", color = 0x0c0c0c )
    

    channel = client.get_channel( 729691962344472596 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.event
async def on_member_remove( member ):
    emb = discord.Embed( description = f"**<:leave:730480292736925716> Пользователь **{member.mention}**, покинул сервер!<:leave:730480292736925716> **", color = 0x0c0c0c )
    

    channel = client.get_channel( 729691962344472596 ) # Айди канала куда будет писаться сообщение
    await channel.send( embed = emb )


@client.event
async def on_message_delete(message):
    channel = client.get_channel(729691763500908636)
    if message.content is None:
        return
    emb = discord.Embed(colour=0xff0000,
                description=f"{message.author}"
                    f"\n Удалил сообщение: `{message.content}`"
                    f"\n В канале: `{message.channel}`",timestamp=message.created_at)


    emb.set_author(name = 'Журнал аудита | Удаление сообщений', url = emb.Empty, icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
    emb.set_footer(text=f'ID Пользователя: {message.author.id} | ID Сообщения: {message.id}')
    await channel.send(embed=emb)
    return



@client.command()
@commands.has_permissions( administrator = True)
async def clear(ctx,amount : int):
	await ctx.channel.purge( limit = amount )
	await ctx.send(embed = discord.Embed(description = f'**<a:pingin:730480224898252840> Удалено сообщений {amount}**', color=0x00FFFF))



@client.command( pass_context = True, aliases=[ "Мут", "мут", "мьют", "Мьют", "mute" ] )
@commands.has_permissions( administrator = True)
async def tempmute(ctx, member : discord.Member, time:int, arg:str, *, reason=None):


	Переменная_размут = f'**Вы были размучены на сервере {ctx.guild.name}**'
	Переменная_мут = f'**Вы были замучены на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
	mute_role = discord.utils.get( ctx.message.guild.roles, id = 730483853453688892 )

	await member.add_roles(mute_role, reason=None, atomic=True)
	await ctx.send(embed = discord.Embed(description = f'**:shield:Мут пользователю {member.mention} успешно выдан на {time}{arg} по причине {reason} :shield:**', color=0x0000FF))
	await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

	if arg == "s":
		await asyncio.sleep(time)          
	elif arg == "m":
		await asyncio.sleep(time * 60)
	elif arg == "h":
		await asyncio.sleep(time * 60 * 60)
	elif arg == "d":
		await asyncio.sleep(time * 60 * 60 * 24)
	elif arg == "y":
		await asyncio.sleep(time * 60 * 60 * 24 * 365)
	elif arg == "v":
		await asyncio.sleep(time * 60 * 60 * 24 * 365 * 100)


	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))
	await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))

@tempmute.error 
async def tempmute_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},укажите пользователя или время**', color=0x0c0c0c))



@client.command()
@commands.has_permissions( administrator = True) 
async def unmute(ctx,member: discord.Member = None): 

	if member is None:

		await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

	else:

		mute_role = discord.utils.get(member.guild.roles, id = 730483853453688892) #Айди роли

	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был вернут доступ к чатам.**', color=0x0c0c0c))    

# Работа с ошибками размута

@unmute.error 
async def unmute_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))


@client.command()
@commands.has_permissions( administrator = True)
async def сказать(ctx, member: discord.Member = None, *, reason=None):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed(description= f'**<a:pingin:730480224898252840><a:pingin:730480224898252840><a:pingin:730480224898252840>{reason}<a:pingin:730480224898252840><a:pingin:730480224898252840><a:pingin:730480224898252840>**', color=0x6fdb9e)
    await member.send(embed=emb)


@сказать.error 
async def сказать(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.channel.purge( limit = 1 )
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.mention},пасаси.**', color=0x0c0c0c))


@client.command( pass_context = True, aliases=[ "av", "аватар", "ав" ] )
async def avatar(ctx, member : discord.Member = None):

         user = ctx.message.author if (member == None) else member

         show_avatar = discord.Embed(description =f' Аватар пользователя {user} ',color=0x00FFFF)
         show_avatar.set_image(url='{}'.format(user.avatar_url))
         await ctx.send(embed=show_avatar)
         await ctx.message.delete()



@client.command( pass_context = True, aliases=[ "mutevoice", "мутвойс", "мьютвойс", "Мьютвойс" ] )
@commands.has_permissions( administrator = True)
async def __voice(ctx, member : discord.Member, time:int, arg:str, *, reason=None):

	Переменная_размут = f'**У вас был снят мут войса на сервере {ctx.guild.name}**'
	Переменная_мут = f'**Вам выдали мут войса на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
	mute_role = discord.utils.get( ctx.message.guild.roles, id = 730734953125380167 )

	await member.add_roles(mute_role, reason=None, atomic=True)
	await ctx.send(embed = discord.Embed(description = f'**:shield:Мут войса пользователю {member.mention} успешно выдан на {time}{arg} по причине {reason} :shield:**', color=0x0000FF))
	await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

	if arg == "s":
		await asyncio.sleep(time)          
	elif arg == "m":
		await asyncio.sleep(time * 60)
	elif arg == "h":
		await asyncio.sleep(time * 60 * 60)
	elif arg == "d":
		await asyncio.sleep(time * 60 * 60 * 24)
	elif arg == "y":
		await asyncio.sleep(time * 60 * 60 * 24 * 365)
	elif arg == "v":
		await asyncio.sleep(time * 60 * 60 * 24 * 365 * 100)


	await member.remove_roles( mute_role )
	await ctx.send(embed = discord.Embed(description = f'**:white_check_mark:Мут войса у пользователя {member.mention} успешно снят!:white_check_mark:**', color=0x800080))
	await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))

@__voice.error 
async def __voice_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},укажите пользователя или время**', color=0x0c0c0c))




@client.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":black_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions( administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
	if member.id == ctx.author.id:
		return await ctx.send("ты даун?")
	if member.id == ctx.guild.owner.id:
		return await ctx.send("Я не буду банить создателя сервера...")
	if ctx.author.top_role.position < member.top_role.position:
		return await ctx.send("Я не буду банить человека который выше тебя по должности!")
	guild_msg=discord.Embed(description=f"{ctx.author.mention} забанил участника {member.mention} по причине: {reason}")
	dm_msg=discord.Embed(description=f"Вы были забанены на сервере {ctx.guild.name}, модератором {ctx.author.mention}, по причине: {reason}")
	if reason is None:
		reason="Не указана"
	await member.ban(member, reason=reason)
	await ctx.send(embed=guild_msg)
	await member.send(embed=dm_msg)

	
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота
