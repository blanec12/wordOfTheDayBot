import os
import sys
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")
API_URL = os.getenv("URL")

client = discord.Client(intents=discord.Intents.default())


async def send_message(msg):
    channel = await client.fetch_channel(CHANNEL)
    await channel.send(msg)
    sys.exit(0)


async def get_word():
    req = requests.get(API_URL)
    data = req.json()

    print(data["word"], data["definitions"])
    print(req.json().keys())


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    await get_word()


if __name__ == "__main__":
    client.run(TOKEN)
