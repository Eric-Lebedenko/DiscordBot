import disnake
from disnake.ext import commands

class RolesPings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles_pings(self, ctx: commands.Context):
        # Purge the command invocation message
        await ctx.channel.purge(limit=1)

        # Create an embed for displaying role pings
        emb = disnake.Embed(title="Role Pings", color=0xFF0000)

        # Add fields for each role with their respective mention
        emb.add_field(name="Boss", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Economist", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Politician", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Trader", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Corruptor", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Investor", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Secret Agent", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Lobbyist", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Seller", value="Mention: <@&roles_id>", inline=False)
        emb.add_field(name="Revolutionary", value="Mention: <@&roles_id>", inline=False)

        # Set footer indicating who provided the role pings
        emb.set_footer(text="By Server Staff")

        # Send the embed to the channel
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(RolesPings(bot))
