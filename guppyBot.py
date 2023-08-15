import discord
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Establish the command prefix
bot = commands.Bot(command_prefix='/guppy ', intents=intents)

# Load Git command data from the JSON
with open('commands.json', 'r') as file:
    gitCommands = json.load(file)

# Log in with the bot
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Define a command to output a list of commands
@bot.command(name='all')
async def guppyAll(ctx):
    # Create a list of all the commands
    allCommands = "\n" + "# Available Commands\n- " + "\n- ".join(gitCommands.keys()) + "\n"
    await ctx.send(allCommands)

# Define a command to output specific commands
@bot.command(name='command')
async def guppyCommand(ctx, *, command=None):
    # Check if the user gave a command
    if command is None:
        await ctx.send("Please provide a Git command for help. For example: `/guppy command git init`")
        return

    # Output the description for the user-defined command
    description = gitCommands.get(command)
    if description:
        await ctx.send(description)
    else:
        await ctx.send(f"Sorry, I don't have information on the command `{command}`. Please check the command and try again.")

# Run the bot
bot.run('TOKEN')
