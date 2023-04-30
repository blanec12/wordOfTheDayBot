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


def prettify_response(info):
    result = f"**{info['word'].title()}**\n"
    for ndx, entry in enumerate(info["definitions"]):
        result += f"{ndx + 1}. ({entry['partOfSpeech']}) - {entry['text']}\n"

    return result


async def send_message(msg):
    channel = await client.fetch_channel(CHANNEL)
    await channel.send(msg)
    sys.exit(0)


async def get_word_info():
    req = requests.get(API_URL)
    info = req.json()
    return prettify_response(info)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    msg_details = await get_word_info()
    await send_message(msg_details)


if __name__ == "__main__":
    client.run(TOKEN)
