#!/usr/bin/python3
import discord
import asyncio
import datetime

#the master client 
client = discord.Client() 
        
@client.event
async def on_ready():
    servers_str = ""
    for server in client.servers:
        servers_str = servers_str + " " + server.name #TODO: server object is weird. Causing crash

    print("{}: Logged in as: {}".format(datetime.datetime.now(), client.user.name))

@client.event
async def on_message(message):
    if message.content.startswith('Hi Tyrone') or message.content.startswith("!hi"):
        await client.send_message(message.channel, "Hi {} or should I say {}".format(message.author, message.author.nick))
    if message.content.startswith("!david"):
        await client.send_message(message.channel, "Oh I don't like that at all David.")
    if message.content.startswith("I think Tyrone does"):
        await client.send_message(message.channel, "I probably do")
    if "tyrone" in message.content.lower():
        print("@{} said \"{}\" in #{}".format(message.author.name, message.content, message.channel))

#TODO: Find a way to define a home base channel. It's somewhere in message
def tyrone_kill():
#    client.send_message(CHANNEL?, "Looks like I got the plug pulled on me...bye!")
    client.close()


#Must be run last
client.run("NDU1MDU4MzA5MjA1MDY1NzI4.Df93Mw.FTrjNE5N0_bUjcKU3UUuFc7i3R8")

