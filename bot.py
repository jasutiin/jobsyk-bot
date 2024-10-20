# This example requires the 'message_content' intent.
from dotenv import load_dotenv
from functions import get_indeed_internships

import os
import discord

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!jobs'):
        jobs = get_indeed_internships()

        for job in jobs:
            await message.channel.send("# " + job.company + "\n*" + job.position + "*\n" + job.location)
            
client.run(token)
