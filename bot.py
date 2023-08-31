import os
import aiohttp

import discord
from discord.ext import commands

from dotenv import load_dotenv

import random

from messages import welcome_messages

# Load token from env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Set up bot
bot = commands.Bot(command_prefix="!", description="Michigan bot", intents=intents)


@bot.event
async def on_ready():
    """Prints when bot is ready"""
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_message(message):
    """Responds to messages containing "Michigan" and ignores itself"""
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

    if "michigan" in message.content.lower():
        user = message.author.display_name
        fact = await get_fact_from_api()
        welcome_message = get_welcome_message(user)
        await message.channel.send(welcome_message + "\n\n" + fact)


async def get_fact_from_api():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://michigan-facts-ts.vercel.app/facts") as resp:
            data = await resp.json()
            fact = data["randomFact"]["content"]
            return fact

def get_welcome_message(user):
    return random.choice(welcome_messages).format(user=user)


bot.run(TOKEN)
