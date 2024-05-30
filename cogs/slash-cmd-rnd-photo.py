import disnake
import requests
from disnake.ext import commands

class Pics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Random photo from the internet")
    async def random_photo(self, ctx):
        # Define subreddit and API endpoint
        subreddit = "pics"
        url = f"https://www.reddit.com/r/{subreddit}/random.json"

        # Set headers and make request to API
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            # Extract data from JSON response
            data = response.json()[0]['data']['children'][0]['data']
            title = data['title']
            url = data['url']

            # Send embed message with photo title and image
            embed = disnake.Embed(title=title)
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error: Could not retrieve photo.")

def setup(bot):
    bot.add_cog(Pics(bot))
