import disnake
from disnake.ext import commands

class ProfileCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.likes = {}
        self.dislikes = {}

    @commands.slash_command(description="Показать профиль пользователя")
    async def profile(self, ctx, member: disnake.Member = None):
        # Check if member is None, set to ctx.author if so
        if member is None:
            member = ctx.author

        guild = ctx.guild

        if guild:
            # Gather user information
            roles = [role.name for role in member.roles if role != guild.default_role]
            roles_str = ", ".join(roles) if roles else "No roles"
            top_role = member.top_role.name

            # Create the embed
            embed = disnake.Embed(title="Профиль Пользователя", color=member.color)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.add_field(name="Имя пользователя", value=member.display_name, inline=False)
            embed.add_field(name="Роли", value=roles_str, inline=False)
            embed.add_field(name="Высшая роль", value=top_role, inline=False)
            embed.add_field(name="Вступил на сервер", value=member.joined_at.strftime("%d.%m.%Y"), inline=False)
            embed.add_field(name="Зарегистрирован в Discord", value=member.created_at.strftime("%d.%m.%Y"), inline=False)
            embed.add_field(name="Количество сообщений", value=len(await ctx.channel.history().flatten()), inline=False)
            embed.set_image(url="https://i.imgur.com/QzB7q9J.png")

            # Add likes and dislikes information
            likes = self.likes.get(member.id, 0)
            dislikes = self.dislikes.get(member.id, 0)
            embed.add_field(name="Лайки", value=f"{likes}", inline=False)
            embed.add_field(name="Дизлайки", value=f"{dislikes}", inline=False)
            status_str = "Не беспокоить" if member.status == disnake.Status.dnd else str(member.status).title()
            embed.add_field(name="Статус", value=status_str, inline=False)

            # Send the embed
            await ctx.send(embed=embed)
        else:
            await ctx.send("Server not found.")

    @commands.slash_command(description="Поставить лайк пользователю")
    async def like(self, ctx, member: disnake.Member):
        # Check for self-like and bot-like
        if member == ctx.author:
            await ctx.send("Вы не можете поставить лайк самому себе.", ephemeral=True)
            return
        if member.bot:
            await ctx.send("Ботам нельзя ставить лайки.", ephemeral=True)
            return

        # Remove dislike if user has already disliked
        if member.id in self.dislikes:
            del self.dislikes[member.id]

        # Check if the user has already been liked
        if member.id in self.likes:
            await ctx.send("Вы уже поставили лайк этому пользователю.", ephemeral=True)
            return

        # Increment likes count for the user
        self.likes[member.id] = self.likes.get(member.id, 0) + 1
        await ctx.send(f"Лайк поставлен пользователю {member.mention}.", ephemeral=True)

    @commands.slash_command(description="Поставить дизлайк пользователю")
    async def dislike(self, ctx, member: disnake.Member):
        # Check for self-dislike and bot-dislike
        if member == ctx.author:
            await ctx.send("Вы не можете поставить дизлайк самому себе.", ephemeral=True)
            return
        if member.bot:
            await ctx.send("Ботам нельзя ставить дизлайки.", ephemeral=True)
            return

        # Remove like if user has already liked
        if member.id in self.likes:
            del self.likes[member.id]

        # Check if the user has already been disliked
        if member.id in self.dislikes:
            await ctx.send("Вы уже поставили дизлайк этому пользователю.", ephemeral=True)
            return

        # Increment dislikes count for the user
        self.dislikes[member.id] = self.dislikes.get(member.id, 0) + 1
        await ctx.send(f"Дизлайк поставлен пользователю {member.mention}.", ephemeral=True)

def setup(bot):
    bot.add_cog(ProfileCog(bot))
