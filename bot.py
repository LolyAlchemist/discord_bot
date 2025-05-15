import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Emoji list
emojis = ["😂", "😼", "😔", "😹", "💀", "😕", "😺", "😾", "👍", "🌟", "😌"]

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f" Logged in as {bot.user}")

@bot.command(name="emoji")
async def emoji_classic(ctx):
    emoji = random.choice(emojis)
    await ctx.send(emoji)

bot.run("MTM3MjY3Nzc5MTk2MjYyODI0Nw.GNZRuz.kIJCocSyKkHuind6TTHgHueIDNBKQUVony229o")
