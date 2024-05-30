import disnake
from disnake.ext import commands

class WelcomeMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def welcome_msg(self, ctx: commands.Context):
        # Delete the command invocation message
        await ctx.channel.purge(limit=1)

        # Construct the formatted welcome banner
        banner = """
```css
╔══════════════════════════════════╗
║       🌟 Mafia & Economy 🌟      ║
║                                  ║
║   Welcome to Mafia & Economy!    ║
║                                  ║
║   This is a place to discuss     ║
║   economics, politics, and       ║
║   strategic role-playing games.   ║
║                                  ║
║   Join us to engage in lively    ║
║   discussions, develop strategic ║
║   thinking, and have fun with    ║
║   like-minded individuals!       ║
║                                  ║
╚══════════════════════════════════╝
```"""

        # Send the welcome banner to the channel
        await ctx.send(banner)

def setup(bot):
    bot.add_cog(WelcomeMessage(bot))
