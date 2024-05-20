import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

@commands.command()
async def user(ctx, *name):
    user = ctx.message.content.removeprefix(".user ")
    page = requests.get(f"https://anilist.co/user/{user}")
    soup = BeautifulSoup(page.text, features="html.parser")
    username = soup.find('h1', attrs={'class':'name'}).string
    avatar = soup.findAll('img', attrs={'class':'avatar'})
    link = avatar[0]
    getlink = link.get('src')
    about = soup.find('div', attrs={'class':'about'}).string
    await ctx.send(f"{username}\n{about} {getlink} ")


async def setup(bot):
    bot.add_command(user)