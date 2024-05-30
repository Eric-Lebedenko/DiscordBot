import os
import disnake
import datetime
import random
from disnake.ext import commands
import config

# Initialize the bot with all intents and specify the command prefix and test guilds
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    test_guilds=[1031991991313104956]  # Replace with your server ID
)

# Voice channel ID to connect the bot to
voice_channel_id = 1239591671721627678  # Replace with your voice channel ID


@bot.event
async def on_ready():
    """
    Event handler for when the bot is ready.
    This function prints the bot's username and connects to the specified voice channel.
    """
    print(f"[{datetime.datetime.now()}] Bot: {bot.user} is online!")

    # Get the voice channel object by its ID
    voice_channel = bot.get_channel(voice_channel_id)

    if voice_channel:
        # Connecting the bot to the voice channel
        await voice_channel.connect()
    else:
        print(f"Voice channel with ID {voice_channel_id} not found!")


@bot.event
async def on_command_error(ctx, error):
    """
    Event handler for command errors.
    This function handles specific command errors and sends appropriate messages to the user.

    Parameters:
    ctx (commands.Context): The context of the command.
    error (commands.CommandError): The error that was raised.
    """
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, you do not have the required permissions to execute this command!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Correct usage of the command: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))


@bot.event
async def on_member_join(member):
    """
    Event handler for when a new member joins the server.
    This function assigns a role to the new member and sends a welcome message.

    Parameters:
    member (disnake.Member): The member that joined.
    """
    emojis = ["🎉", "👋", "🎂", "🎊", "🥳", "🤗", "😄", "🤝", "🙌"]

    guild = bot.get_guild(config.GUILD)  # Replace with your server ID
    channel = bot.get_channel("welcome channel ID")  # Replace with your welcome channel ID
    emoji = random.choice(emojis)

    # Role to assign to the new member
    role = guild.get_role("role ID")  # Replace with your role ID

    # Add the role to the new member
    await member.add_roles(role)

    # Create and send the welcome embed
    embed = disnake.Embed(
        title="Welcome!",
        description=f"\n<@{member.id}>\n*Enjoy your stay!*\n*Have a good time!*",
        color=0x00FFFF,
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    message = await channel.send(embed=embed)
    await message.add_reaction(emoji)


# Load all cogs from the cogs directory
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

# Run the bot using the token from config.py
bot.run(config.BOT_TOKEN)
