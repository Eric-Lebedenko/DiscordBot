import disnake
from disnake.ext import commands

class RolesInfoEveryone(commands.Cog):
    """
    A cog for providing information about bot commands to everyone.

    This cog includes a command that can be used by administrators to send an embed
    with detailed information about various bot commands to a channel.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def evr_roles_info(self, ctx: commands.Context):
        """
        Command to send an embed with information about bot commands.

        This command clears the command message and sends an embed with detailed
        information about various bot commands available on the server.

        Parameters:
        ctx (commands.Context): The context in which the command was invoked.
        """
        await ctx.channel.purge(limit=1)

        # Create the embed with command information
        emb = disnake.Embed(
            title="Bot Commands",
            description="by <@1079049758657753098>",
            colour=disnake.Colour.blue()
        )
        emb.add_field(
            name="</avatar:1086439082848178266> <@user> - Get any member's avatar from the server",
            value="",
            inline=False
        )
        emb.add_field(
            name="</random_photo:1086439083192094753> - Get a random photo from the internet.",
            value="",
            inline=False
        )
        emb.add_field(
            name="</random_meme:1086439083192094751> - Get a random MEME from the internet.",
            value="",
            inline=False
        )
        emb.add_field(
            name="</report:1086439083192094752> <text> - Send a report. _This command can be used in any channel._",
            value="",
            inline=False
        )
        emb.add_field(
            name="",
            value="**All commands are available for use in the channel:** \n<#1079522250627223602>",
            inline=False
        )
        emb.set_thumbnail(url="https://i.imgur.com/09u6Wuc.png")
        emb.set_footer(text="By Server Staff")

        await ctx.send(embed=emb)

# Function to set up the cog
def setup(bot):
    bot.add_cog(RolesInfoEveryone(bot))
