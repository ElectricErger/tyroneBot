import discord
import asyncio

#the master client 
client = discord.Client() 

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-----------")

@client.event
async def on_message(message):
    if message.content.startswith('Hi Tyrone') or message.content.startswith("!hi"):
        await client.send_message(message.channel, "Hi {}".format(message.author))
    if message.content.startswith("!david"):
        await client.send_message(message.channel, "Oh I don't like that at all David.")

client.run("NDU1MDU4MzA5MjA1MDY1NzI4.Df93Mw.FTrjNE5N0_bUjcKU3UUuFc7i3R8")
