import disnake
from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(usage="clear <amount>", description="Clear messages")
    @commands.has_permissions(administrator=True)
    async def clear(self, interaction, amount: int):
        # Send a message indicating the number of messages to be deleted
        await interaction.response.send_message(f"Deleting {amount} messages.")

        # Purge the specified number of messages
        await interaction.channel.purge(limit=amount + 1)


def setup(bot):
    # Add the cog to the bot
    bot.add_cog(Clear(bot))
