import discord
import json
import os
from discord.ext import commands

myKey = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

# Establish the command prefix
bot = commands.Bot(command_prefix="/guppy ",
                   intents=intents,
                   help_command=None)

# Load Git command data from the JSON
with open("commands.json", "r") as file:
  gitCommands = json.load(file)


# Log in with the bot
@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")


# Define a command to display the bot commands
@bot.command(name="help")
async def guppyHelp(ctx):
  embed = discord.Embed(
    title="Guppy Help",
    description="Here are the commands you can use with Guppy:",
    color=0x00ff00)

  for command in bot.commands:
    # Skip the help command to prevent redundancy
    if command.name == "help":
      continue
    embed.add_field(name=f"/guppy {command.name}",
                    value=command.brief or "No description provided.",
                    inline=False)

  await ctx.send(embed=embed, delete_after=30)
  await ctx.message.delete(delay=30)


# Define a command to output a list of commands
@bot.command(name="all", brief="Lists all available Git commands.")
async def guppyAll(ctx):
  embed = discord.Embed(title="Available Git Commands", color=0x00ff00)

  # Add each command as a field
  for command, description in gitCommands.items():
    if len(
        description
    ) > 1024:  # Trim the description if it exceeds the field value limit
      description = description[:1020] + "..."

    embed.add_field(name=command, value=description, inline=False)

  # Check if there are too many fields, and if so, send a message to inform the user
  if len(gitCommands) > 25:
    await ctx.send(
      "There are too many commands to display in one embed. Please refer to the documentation or try specific commands."
    )
    return

  await ctx.send(embed=embed, delete_after=30)
  await ctx.message.delete(delay=30)


# Define a command to output specific commands
@bot.command(name="command",
             brief="Provides a description for a given Git command.")
async def guppyCommand(ctx, *, command=None):
  if command is None:
    embed = discord.Embed(
      title="Error",
      description=
      "Please provide a Git command for help. For example: `/guppy command init`",
      color=0xff0000)
  else:
    description = gitCommands.get(command)
    if description:
      embed = discord.Embed(title=f"Git Command: {command}",
                            description=description,
                            color=0x00ff00)
    else:
      embed = discord.Embed(
        title="Error",
        description=
        f"Sorry, I don't have information on the command `{command}`. Please check the command and try again.",
        color=0xff0000)
  await ctx.send(embed=embed, delete_after=30)
  await ctx.message.delete(delay=30)


# Handle erroneous user inputs
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    embed = discord.Embed(
      title="Error",
      description=
      "Sorry, that command doesn't seem to exist. Use `/guppy help` for a list of available commands.",
      color=0xff0000)
    await ctx.send(embed=embed, delete_after=30)
    await ctx.message.delete(delay=30)


# Run the bot
bot.run(myKey)