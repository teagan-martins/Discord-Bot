import discord
from discord.ext import commands
import random
import requests
import bs4

token_file = open('token.txt','r')
token = token_file.readline()
token_file.close()

facts = open('facts.txt', 'r')
facts_list = facts.readlines()
facts.close()

count = 0
for line in facts_list:
    facts_list[count] = facts_list[count].rstrip()
    count+=1

bot = discord.Client()
vbot = commands.Bot('$')

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_message(message):

    if message.content.lower() == "$jimmypic":
        num = random.randint(1,4)
        if num == 1:
            with open("Jimmy1.JPG", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 2:
             with open("Jimmy2.jpg", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 3:
            with open("Jimmy3.jpg", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)
        elif num == 4:
            with open("Jimmy4.PNG", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)

    if message.content.lower() == "$coin":
        coin = random.randint(1,2)
        if coin == 1:
            await message.channel.send("Heads :coin:")
        elif coin == 2:
            await message.channel.send("Tails :coin:")

    if message.content.lower() == "$dice":
        dice = random.randint(1,6)
        if dice == 1:
            await message.channel.send("1 :game_die:")
        elif dice == 2:
            await message.channel.send("2 :game_die:")
        elif dice == 3:
            await message.channel.send("3 :game_die:")
        elif dice == 4:
            await message.channel.send("4 :game_die:")
        elif dice == 5:
            await message.channel.send("5 :game_die:")
        elif dice == 6:
            await message.channel.send("6 :game_die:")

    if message.content.lower()[0:7] == '$avatar':
        user_avatar = await bot.fetch_user(int(message.content[7:]))
        print(user_avatar)
        await message.channel.send(user_avatar.avatar_url_as(format=None, static_format='webp', size=1024))

    if message.content.lower() == '$fact':
        num = random.randint(1,3090)
        await message.channel.send(facts_list[num])

    if message.content.lower()[0:7] == '$search':
        keyword = message.content.lower()[7:]
        url = requests.get("https://images.search.yahoo.com/search/images?p=" + keyword)
        soup = bs4.BeautifulSoup(url.text, 'lxml')

        num = random.randint(0,len(soup))

        photo_url = soup.select('.results li.ld .img')[num]

        photo_url = str(photo_url)
        datasrc = photo_url.find('data-src')
        shortened_element = (photo_url[datasrc:])
        quote_list = [quote for quote in range(len(shortened_element)) if shortened_element.startswith('"', quote)]

        await message.channel.send(shortened_element[quote_list[0]+1:quote_list[1]])


    if message.author.id == USER ID HERE:
        await message.channel.send('YOUR MESSAGE HERE')

    if message.author.id == USER ID HERE:
        await message.channel.send('YOUR MESSAGE HERE')


    if message.content.lower() == "$commands":
        await message.channel.send("Commands:\n$JimmyPic - Send a random picture of Jimmy\n$Coin - Flip a coin\n$Dice - Roll a die\n$Avatar(userID) - Send an enlarged picture of someone's avatar\n$Fact - Send a random fun fact\n*Commands are not case-sensitive*")


bot.run(token)
