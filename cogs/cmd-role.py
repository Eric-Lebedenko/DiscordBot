import disnake
from disnake.ext import commands


class SelectGames(disnake.ui.Select):
    def __init__(self):
        # Define the options for the dropdown menu
        options = [
            disnake.SelectOption(label="Economist", value="ROLES_ID"),
            disnake.SelectOption(label="Politician", value="ROLES_ID"),
            disnake.SelectOption(label="Trader", value="ROLES_ID"),
            disnake.SelectOption(label="Corrupt", value="ROLES_ID"),
            disnake.SelectOption(label="Investor", value="ROLES_ID"),
            disnake.SelectOption(label="Secret Agent", value="ROLES_ID"),
            disnake.SelectOption(label="Lobbyist", value="ROLES_ID"),
            disnake.SelectOption(label="Seller", value="ROLES_ID"),
            disnake.SelectOption(label="Revolutionary", value="ROLES_ID")
        ]
        # Initialize the Select component
        super().__init__(
            placeholder="Select a role", options=options, custom_id="games", min_values=0, max_values=1
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        # Defer the interaction response
        await interaction.response.defer()
        # Define all possible role IDs
        all_roles = {
            "ROLES_ID", "ROLES_ID", "ROLES_ID",
            "ROLES_ID", "ROLES_ID", "ROLES_ID",
            "ROLES_ID", "ROLES_ID", "ROLES_ID"
        }
        # Lists to store roles to add and remove
        to_remove = []
        to_add = []

        if not interaction.values:
            # If no roles are selected, remove all roles
            for role_id in all_roles:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            await interaction.author.remove_roles(*to_remove, reason="Removed all roles")

        else:
            # If roles are selected, process the selection
            chosen_roles = {int(value) for value in interaction.values}
            ids_to_remove = all_roles - chosen_roles

            for role_id in ids_to_remove:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            for role_id in chosen_roles:
                role = interaction.guild.get_role(role_id)
                to_add.append(role)

            await interaction.author.remove_roles(*to_remove, reason="Removed roles")
            await interaction.author.add_roles(*to_add, reason="Added roles")


class GameRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    async def games(self, ctx):
        # Create a view with the SelectGames component
        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        # Create an embed with role information and instructions
        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Mafia & Economy Server Roles:")
        embed.description = ("Before selecting a role, please familiarize yourself with the rules and role descriptions "
                             "of the Mafia & Economy server. After that, choose the role that suits you best. You can "
                             "only choose one role.\n\nNote: It may take a few seconds for <@1079049758657753098> to "
                             "assign you a role. Please be patient.")
        embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        # Send the embed with the view
        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        # Add the SelectGames view persistently
        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        self.bot.add_view(view, message_id="message_id")


def setup(bot):
    bot.add_cog(GameRoles(bot))
