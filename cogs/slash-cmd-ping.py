from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Ping command")
    @commands.has_permissions(administrator=True)
    async def ping(self, interaction):
        # Respond with "Pong!"
        await interaction.response.send_message("Pong!")

def setup(bot):
    # Add the Ping cog to the bot
    bot.add_cog(Ping(bot))
