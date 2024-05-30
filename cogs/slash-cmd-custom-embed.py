import disnake
from disnake.ext import commands

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Custom Embed")
    @commands.has_permissions(administrator=True)
    async def custom_embed(self, ctx, title: str, text: str, footer: str = "By Server Staff", color: str = "0xfffff"):
        # Set the color of the embed
        color_mapping = {
            "red": 0xFF0000,
            "green": disnake.Color.green(),
            "blue": disnake.Color.blue(),
            "orange": disnake.Color.orange(),
            "purple": disnake.Color.purple(),
            "cyan": 0x00CED1
        }
        color = color_mapping.get(color.lower(), None)

        # Create a new embed object with the given components and color
        embed = disnake.Embed(title=title, description=text, color=color)
        embed.set_footer(text=footer)

        # Send the embed message
        await ctx.send(embed=embed)

def setup(bot):
    # Add the cog to the bot
    bot.add_cog(EmbedCog(bot))
