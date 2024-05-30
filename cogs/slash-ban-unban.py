import disnake
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Ban a user")
    @commands.has_permissions(administrator=True)
    async def ban(self, interaction, user: disnake.User, *, reason=None):
        # Ban the user from the guild
        await interaction.guild.ban(user, reason=reason)

        # Send an ephemeral message indicating the user is banned
        await interaction.response.send_message(f"{user.mention} has been banned.", ephemeral=True)

    @commands.slash_command(description="Unban a user")
    @commands.has_permissions(administrator=True)
    async def unban(self, interaction, user: disnake.User):
        # Unban the user from the guild
        await interaction.guild.unban(user)

        # Send an ephemeral message indicating the user is unbanned
        await interaction.response.send_message(f"{user.mention} has been unbanned.", ephemeral=True)


def setup(bot):
    # Add the cog to the bot
    bot.add_cog(Ban(bot))
