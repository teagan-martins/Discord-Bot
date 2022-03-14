import random
from asyncio import sleep
import bs4
import discord
import matplotlib.pyplot as plt
import requests

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


    if message.author.id == 371022437883707392:
        chance = random.randint(1,50)
        if chance == 14:
            await message.channel.send('Hello Nathan')

    if message.author.id == 271426173781671937:
        chance2 = random.randint(1,50)
        if chance2 == 23:
            await message.channel.send('Hello Jimmy')

    if message.content.lower()[0:5] == '$spam' and message.author.id == 467042361881395200:
        slash_list = [slash for slash in range(len(message.content.lower())) if message.content.lower().startswith("/",slash)]

        num_spam = int(message.content[slash_list[0]+1:slash_list[1]])

        await message.delete()

        for x in range(num_spam):
            await message.channel.send(message.content[slash_list[1]+1:])

    if message.content.lower()[0:5] == '$poll':
        slash_list = [slash for slash in range(len(message.content.lower())) if message.content.lower().startswith("/",slash)]

        option_count = len(slash_list)-1

        option_list = []
        for x in slash_list:
            option_list.append(x)

        option_list.pop(0)

        if option_count==1:
           bot_message = await message.channel.send(message.content[slash_list[0]+1:slash_list[1]] + '\n' + ':red_circle: = ' + message.content[slash_list[1]+1:])
           await bot_message.add_reaction('🔴')

           await sleep(10)
           bot_msg = discord.utils.get(bot.cached_messages, id=bot_message.id)
           rcreaction = discord.utils.get(bot_msg.reactions, emoji='🔴')

           plt.bar([message.content[slash_list[1]+1:]],[rcreaction.count-1], color = ['salmon'])

           plt.xlabel('Options')
           plt.ylabel('Count')
           plt.title(message.content[slash_list[0]+1:slash_list[1]])
           plt.savefig('bar.png')
           plt.clf()

           with open("bar.png", 'rb') as f:
               picture = discord.File(f)
               await message.channel.send(file = picture)

        elif option_count==2:
            bot_message = await message.channel.send(message.content[slash_list[0]+1:slash_list[1]] + '\n' + ':red_circle: = ' + message.content[slash_list[1]+1:slash_list[2]] + '\n' + ':blue_circle: = ' + message.content[slash_list[2]+1:])
            await bot_message.add_reaction('🔴')
            await bot_message.add_reaction('🔵')

            await sleep(10)

            bot_msg = discord.utils.get(bot.cached_messages, id=bot_message.id)
            rcreaction = discord.utils.get(bot_msg.reactions, emoji='🔴')
            bcreaction = discord.utils.get(bot_msg.reactions, emoji='🔵')

            plt.bar([message.content[slash_list[1]+1:slash_list[2]], message.content[slash_list[2]+1:]],[rcreaction.count-1,bcreaction.count-1], color = ['salmon','cornflowerblue'])

            plt.xlabel('Options')
            plt.ylabel('Count')
            plt.title(message.content[slash_list[0]+1:slash_list[1]])
            plt.savefig('bar.png')
            plt.clf()

            with open("bar.png", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)

        elif option_count==3:
           bot_message =  await message.channel.send(message.content[slash_list[0]+1:slash_list[1]] + '\n' + ':red_circle: = ' + message.content[slash_list[1]+1:slash_list[2]] + '\n' + ':blue_circle: = ' + message.content[slash_list[2]+1:slash_list[3]] + '\n' + ':yellow_circle: = ' + message.content[slash_list[3]+1:])
           await bot_message.add_reaction('🔴')
           await bot_message.add_reaction('🔵')
           await bot_message.add_reaction('🟡')

           await sleep(10)

           bot_msg = discord.utils.get(bot.cached_messages, id=bot_message.id)
           rcreaction = discord.utils.get(bot_msg.reactions, emoji='🔴')
           bcreaction = discord.utils.get(bot_msg.reactions, emoji='🔵')
           ycreaction = discord.utils.get(bot_msg.reactions, emoji='🟡')

           plt.bar([message.content[slash_list[1]+1:slash_list[2]], message.content[slash_list[2]+1:slash_list[3]], message.content[slash_list[3]+1:]],[rcreaction.count-1,bcreaction.count-1,ycreaction.count-1], color = ['salmon','cornflowerblue','gold'])

           plt.xlabel('Options')
           plt.ylabel('Count')
           plt.title(message.content[slash_list[0]+1:slash_list[1]])
           plt.savefig('bar.png')
           plt.clf()

           with open("bar.png", 'rb') as f:
               picture = discord.File(f)
               await message.channel.send(file = picture)

        elif option_count==4:
            bot_message = await message.channel.send(message.content[slash_list[0]+1:slash_list[1]] + '\n' + ':red_circle: = ' + message.content[slash_list[1]+1:slash_list[2]] + '\n' + ':blue_circle: = ' + message.content[slash_list[2]+1:slash_list[3]] + '\n' + ':yellow_circle: = ' + message.content[slash_list[3]+1:slash_list[4]] + '\n' + ':green_circle: = ' + message.content[slash_list[4]+1:])
            await bot_message.add_reaction('🔴')
            await bot_message.add_reaction('🔵')
            await bot_message.add_reaction('🟡')
            await bot_message.add_reaction('🟢')

            await sleep(10)

            bot_msg = discord.utils.get(bot.cached_messages, id=bot_message.id)

            rcreaction = discord.utils.get(bot_msg.reactions, emoji='🔴')
            bcreaction = discord.utils.get(bot_msg.reactions, emoji='🔵')
            ycreaction = discord.utils.get(bot_msg.reactions, emoji='🟡')
            gcreaction = discord.utils.get(bot_msg.reactions, emoji='🟢')


            plt.bar([message.content[slash_list[1]+1:slash_list[2]], message.content[slash_list[2]+1:slash_list[3]], message.content[slash_list[3]+1:slash_list[4]], message.content[slash_list[4]+1:]],[rcreaction.count-1,bcreaction.count-1,ycreaction.count-1,gcreaction.count-1], color = ['salmon','cornflowerblue','gold','limegreen'])
            plt.xlabel('Options')
            plt.ylabel('Count')
            plt.title(message.content[slash_list[0]+1:slash_list[1]])
            plt.savefig('bar.png')
            plt.clf()

            with open("bar.png", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file = picture)

    if message.content.lower() == "$commands":
        await message.channel.send("Commands:\n$jimmypic - Send a random picture of Jimmy\n$coin - Flip a coin\n$dice - Roll a die\n$avatar(userID) - Send an enlarged picture of someone's avatar\n$fact - Send a random fun fact\n$search(word/string) - Send a random image off Yahoo Images related to that specified search term\n$poll/question/option/option/option/option - Sends a poll for members to react to. Sends a bar graph representing the answers as well. Allows a question with up to 4 options.\n*Commands are not case-sensitive*")

bot.run(token)
