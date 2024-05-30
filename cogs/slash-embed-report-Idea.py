import disnake
from disnake.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Отправка жалобы или идеи на сервер")
    @commands.has_permissions(administrator=True)
    async def emb(self, interaction):
        # Create an embed with the specified title, description, and color
        emb = disnake.Embed(
            title="Появилася идея? Нужна помощь?",
            description="\n\n**• Здесь ты можешь предложить свою идею которую, мы возможно воплотим на нашем сервере.**"\
                        "\n\n**• Здесь ты можешь отправить отчёт / жалобу на человека который нарушает правила серверa / Discord.**"\
                        "\n\n\n 💢Жалобы невидимы для пользователей. \nПосле отправки жалобы с Вами свяжеться Сотрудник сервера и Вы сможете пообщаться с ним в отдельном приватном чате."\
                        "\n 💡Идеи будут отправлены в канал: <#1087106832167870506> \nГде Вы и другие учасники сервера смогут проголосовать за Вашу идею, а так же автоматически с Вашей идеей будет уведомлен сотрудники сервера."\
                        "\n\n _P.s Ваши Жалобы / Отчёты / Предложения очень ВАЖНЫ для нас_ \n**Просьба перед отправкой тщательно обдумать содержимое Вашего письма**",
            color=0xffffff
        )
        emb.set_footer(text="By Server Staff")  # Set the footer text

        # Send the embed message as a response to the interaction
        await interaction.response.send_message(embed=emb)


def setup(bot):
    bot.add_cog(Embed(bot))
