import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    guild = discord.Object(id=1199168199338508449)  # Replace YOUR_GUILD_ID with the actual guild ID
    await bot.tree.sync(guild=guild)  # Sync commands to a specific guild
    print("Commands synced to the guild.")
    for cmd in bot.tree.get_commands():
        print(f"Registered command: {cmd.name}")

@bot.tree.command(name="test", description="A test command")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("Test command works!")

with open("token.txt", "r") as f:
    TOKEN = f.read()
bot.run(TOKEN) 