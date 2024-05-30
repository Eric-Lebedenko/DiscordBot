from disnake.ext import commands
import disnake


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Show Avatar")
    async def avatar(self, interaction, member: disnake.Member = None):
        # If member is not specified, default to the author of the interaction
        user = member or interaction.author

        # Create an embed to display the avatar
        emb = disnake.Embed(title=f"@{user.name}'s Avatar", color=0x2f3136)
        emb.set_image(url=user.display_avatar.url)

        # Send the embed as a response
        await interaction.response.send_message(embed=emb)


def setup(bot):
    # Add the cog to the bot
    bot.add_cog(Avatar(bot))
