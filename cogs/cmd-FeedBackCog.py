import disnake
from disnake.ext import commands

class FeedbackCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def feedback(self, ctx):
        # Delete the command message
        await ctx.channel.purge(limit=1)

        # Create an Embed
        embed = disnake.Embed(
            title="Feedback Form",
            description="Please fill out [this form](https://forms.gle/h4caqq4bVY1CqirL9) to share your feedback and suggestions for our server.",
            color=0x00ff00  # Green color
        )

        # Add a field with information about the feedback form
        embed.add_field(name="Feedback Form", value="[Submit Feedback](https://forms.gle/h4caqq4bVY1CqirL9)")

        # Send the Embed
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FeedbackCog(bot))
