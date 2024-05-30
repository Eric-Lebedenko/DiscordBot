import disnake
from disnake.ext import commands

class RecruitementModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg  # The argument passed to the constructor of the RecruitementSelect class
        components = [
            disnake.ui.TextInput(label="Your text", placeholder="Example text...", custom_id="text")
        ]
        if self.arg == "report":
            title = "Fill out the form to submit a complaint"
            super().__init__(title=title, components=components, custom_id="recruitementModal")
        if self.arg == "idea":
            title = "Fill out the form to submit an idea"
            super().__init__(title=title, components=components, custom_id="recruitementModal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        text = interaction.text_values["text"]
        embed = disnake.Embed(color=0x2F3136, title="Application submitted!")
        embed.description = f"{interaction.author.mention}, Thank you for your **application**! "
        embed.set_thumbnail(url=interaction.author.display_avatar.url)
        if self.arg == "idea":
            await interaction.response.send_message(embed=embed, ephemeral=True)
            channel = interaction.guild.get_channel("channel_id")  # Insert the channel ID where idea submissions will be sent
            msg = await channel.send(f"Idea from {interaction.author.mention} \n\n{text}\n\n<@&ROLES_ID> | <@&ROLES_ID>")
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        if self.arg == "report":
            overwrites = {
                interaction.guild.default_role: disnake.PermissionOverwrite(read_messages=False),
                interaction.guild.me: disnake.PermissionOverwrite(read_messages=True, send_messages=True),
                interaction.author: disnake.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            category = interaction.guild.get_channel("channel_id")
            # create a new room with the name "report-room" and the specified permission overwrites
            new_channel = await category.create_text_channel(f"{interaction.author.display_name}-Report",
                                                             overwrites=overwrites)

            await interaction.response.send_message(embed=embed, ephemeral=True)
            await new_channel.send(
                f"**Report from** {interaction.author.mention} \n\nReport Text:\n{text}\n\n<ROLES>")


class RecruitementSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="💢Complaint", value="report", description="Submit a complaint"),
            disnake.SelectOption(label="💡Idea", value="idea", description="Submit an idea"),
        ]
        super().__init__(
            placeholder="Choose the required form to submit", options=options, min_values=0, max_values=1, custom_id="recruitement"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(RecruitementModal(interaction.values[0]))


class Recruitement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def recruit(self, ctx):
        await ctx.channel.purge(limit=1)
        view = disnake.ui.View()
        view.add_item(RecruitementSelect())

        await ctx.send('Forms for submission:', view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(RecruitementSelect())
        self.bot.add_view(view, message_id="message_id")  # Insert the message ID that will be sent after using the command !recruit

def setup(bot):
    bot.add_cog(Recruitement(bot))
