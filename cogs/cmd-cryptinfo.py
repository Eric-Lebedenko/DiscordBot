import disnake
from disnake.ext import commands

class RolesInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles_info(self, ctx: commands.Context):
        # Clear the command message
        await ctx.channel.purge(limit=1)

        # Create an embed message
        emb = disnake.Embed(title="Link to all roles of the Mafia & Economy server", color=0xFF0000)
        emb.add_field(name="**4. Role Links**", value="", inline=False)

        # Add information about roles to the embed message
        roles_info = [
            {"name": "🕴️ Boss", "mention": "<@&1239609869904908359>", "description": "The main mobster of the server. Has access to all voice and text channels."},
            {"name": "💼 Economist", "mention": "<@&1239610610203754506>", "description": "Expert in finance. Has access to all text channels and to voice channels related to the economy."},
            # Add the remaining roles here
        ]
        for role in roles_info:
            emb.add_field(name=role["name"], value=f'Mention: {role["mention"]}\nDescription: {role["description"]}', inline=False)

        # Add channels information to the embed message
        channels_info = {
            "Bosses": "<#1239613741134512298>",
            "Economists": "<#1239614127173800079>, <#1239614783133581474>, <#1239615416796708956>",
            # Add the remaining channels here
        }
        for role, channels in channels_info.items():
            emb.add_field(name=f"Text channels for {role}:", value=channels, inline=False)

        # Set the footer of the embed message
        emb.set_footer(text="By Server Staff")
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(RolesInfo(bot))
