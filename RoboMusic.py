import discord
from discord.ext import commands,tasks
from asyncio import *


intents = discord.Intents.all()
class Configuration :
    token = "Your Token From Discord Dev"
    prefix = "."


client = commands.Bot(command_prefix=Configuration.prefix,intents=intents)
client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching,name="YOU"))
    print("Hey You")
@client.command()
async def bia(infox,*,values):
    mention = infox.author.mention
    if values == "Admin":
        await infox.send(f"{mention} man omadam")
        print("omad")
    else:
        await infox.send(f"{mention} dobare talash kon")

@client.command()
async def boro(infox, *,values):
    mention = infox.author.mention
    if values == "Admin":
        await infox.send(f"{mention} man omadam")
        print("raft")
    else:
        await infox.send(f"{mention} dobare talash kon")

@client.command(aliases=["guide"])
async def help(infox):
    mention = "RoboMusic"

    desc= """
    My Commands :
    .bia [Admin] 
    .boro [Admin]
    .activity [Game]
    .status [Game]
    .profile
    .come
    .play
    .disc
     """
    pic = "https://i.postimg.cc/FsPsVDb2/Dream-Shaper-v7-a-bot-while-singing-music-as-DJ-0.jpg"
    RoboMusic = discord.Embed(
        title=mention,
        description=desc
    )
    RoboMusic.set_image(url=pic)
    await infox.send(embed=RoboMusic)

@client.command()
async def status(infox, status_type):
    if status_type=="idle" :
        await client.change_presence(status=discord.Status.idle)
    elif status_type == "dnd":
        await client.change_presence(status=discord.Status.dnd)
    else :
        await client.change_presence(status=discord.Status.online)

@client.command(aliases=["act"])
async def activity(infox, activity_type,*, activity_text):
    if activity_type=="watching" :
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching ,name=activity_text))
    elif activity_type == "listening" :
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_text))
    elif activity_type == "streaming":
        await client.change_presence(activity=discord.Streaming(name=activity_text, url='https://www.twitch.tv/twitch'))
    elif activity_type == "playing":
        await client.change_presence(activity=discord.Game(name=activity_text))
    else :
        await infox.send("bbin dash ino: '"+activity_type+" "+activity_text+"' khube man in karo ba khodet anjam bedam ?")

@client.command(aliases=['profile',"bio"])
async def prof(infox):
    mention = infox.author.mention
    id = infox.author
    pic = infox.author.avatar
    embed = discord.Embed(
        title= id ,
        description= mention
    )
    embed.set_image(url=pic)
    embed.set_footer(text="See You Soon 😊")
    await infox.send(embed=embed)



@client.command()
async def come(infox):
    mychannel=infox.message.author.voice.channel
    await mychannel.connect()
    await infox.send("I'm Ready ! ")

@client.command()
async def play(infox,*,track):
    mychannel=infox.message.author.voice.channel
    await mychannel.connect()
    global musicname
    musicname = track
    source = rf'F:\Musics\Spotify\{musicname}.mp3'
    object = discord.utils.get(client.voice_clients, guild=infox.guild)
    await infox.send(f"Playing {musicname} 🎶")
    await client.change_presence(activity=discord.Game(name="MUSIC"))
    if object :
        object.play(discord.FFmpegPCMAudio(source))
    else :
        await infox.send("There is no listener")

@client.command()
async def repeat(infox):
    source = rf'F:\Musics\Spotify\{musicname}.mp3'
    object = discord.utils.get(client.voice_clients, guild=infox.guild)
    await infox.send(f"Playing {musicname} 🎶")
    await client.change_presence(activity=discord.Game(name="MUSIC"))
    object.play(discord.FFmpegPCMAudio(source),after=lambda loop:client.loop.create_task(repeat(infox)))

@client.command()
async def disc(infox):
    mychannel = infox.message.author.voice.channel
    object = discord.utils.get(client.voice_clients, guild=infox.guild)
    await object.disconnect()
    await infox.send("Stoping 📛")

@client.event
async def on_command_error(infox,error):
    if isinstance(error,commands.CommandNotFound):
        await infox.send("Command is Wrong")


client.run(Configuration.token)

