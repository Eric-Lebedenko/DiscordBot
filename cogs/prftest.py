import disnake
from disnake.ext import commands


class ActivityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Define the activity text and type
        activity_text = "Mafia & Economy"
        activity_type = disnake.ActivityType.watching

        # Create an Activity object
        activity = disnake.Activity(type=activity_type, name=activity_text)

        # Set the bot's activity
        await self.bot.change_presence(activity=activity)

        # Print a message indicating that the activity is set
        print("System: Activity set!")


def setup(bot):
    # Add the cog to the bot
    bot.add_cog(ActivityCog(bot))
