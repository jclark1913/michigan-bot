import aiohttp
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from messages import welcome_messages

import random


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

    if "michigan" in message.content.lower():
        user = message.author.display_name
        fact = await get_fact_from_api()
        welcome_message = get_welcome_message(user)
        await message.reply(welcome_message + "\n\n" + fact)


async def get_fact_from_api():
    """Makes a request to the Michigan facts API and returns a random fact"""
    async with aiohttp.ClientSession() as session:
        async with session.get("https://michigan-facts-ts.vercel.app/facts") as resp:
            data = await resp.json()
            fact = data["randomFact"]["content"]
            return fact


def get_welcome_message(user):
    """Returns a random welcome message"""
    return random.choice(welcome_messages).format(user=user)


bot.run(TOKEN)
