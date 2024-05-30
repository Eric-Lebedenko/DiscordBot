import disnake
from disnake.ext import commands


class Ticket:
    def __init__(self, author, category_id, message):
        self.author = author
        self.category_id = category_id
        self.message = message
        self.channel = None

    async def create_ticket(self):
        # Get the category channel where the ticket will be created
        category = self.author.guild.get_channel(self.category_id)

        # Check if the category exists
        if category is None:
            return None

        # Create a new text channel in the specified category
        ticket_channel = await category.create_text_channel(f"{self.author.name}-Ticket")

        # Add permissions for the author to view and send messages in the channel
        await ticket_channel.set_permissions(self.author, read_messages=True, send_messages=True)

        # Save the channel to the ticket object
        self.channel = ticket_channel

        # Send a welcome message to the channel
        await ticket_channel.send(
            f"**Ticket from** {self.author.mention}\n\nTicket Message:\n{self.message}\n\n<@&1079459001714102352>\n_This ticket was created using /report_")

        return ticket_channel


class TicketSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.category_id = "category_id"  # Replace with the ID of the category for the tickets

    @commands.slash_command(description="Submit a Report")
    async def report(self, ctx, *, message: str):
        # Create a new ticket object
        ticket = Ticket(ctx.author, self.category_id, message)

        # Create a new channel for the ticket and send a welcome message
        ticket_channel = await ticket.create_ticket()

        # Send a confirmation message to the author
        if ticket_channel:
            await ctx.send(
                f"Your report has been submitted, {ctx.author.mention}. A staff member will contact you shortly.",
                ephemeral=True)
        else:
            await ctx.send("Failed to create ticket channel. Please contact the server administrator.", ephemeral=True)


def setup(bot):
    bot.add_cog(TicketSystem(bot))
