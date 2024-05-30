import disnake
from disnake.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        usage="kick <@user> <reason>",
        description="Kick a user"
    )
    @commands.has_permissions(administrator=True)
    async def kick(self, interaction, user: disnake.User, *, reason=None):
        # Kick the user from the guild with the given reason
        await interaction.guild.kick(user, reason=reason)
        # Send an ephemeral response confirming the action
        await interaction.response.send_message(f"{user.mention} has been kicked", ephemeral=True)

def setup(bot):
    # Add the cog to the bot
    bot.add_cog(Kick(bot))
