import asyncio
import logging
import sympy
import os
import random
import discord
from discord.ext import commands
import re
from random import sample



intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="f?", intents=intents)
lucky_winner_count = 0
rigged_lucky_winner_count = 0
daily_count = 0

async def on_ready():
    print("The bot is online! Ready to start yapping!")



#EMOJIS
yaw = '<:yaw:1202454187733028874>'
Jimmy = '<:jimothy:1202458237367099402>'
dinoyell = '<:dinoyell:1202619745942245396>'


def splittxt(text, length):
    sentences = (sentence + ". "
                 for sentence in text.split(". "))
    current_line = ""
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if len(current_line + word) <= length:
                current_line += word + " "
            else:
                yield current_line
                current_line = word + " "
        if current_line:
            yield current_line
            current_line = ""
    if current_line:
        yield current_line


with open("perms/admin.txt") as f:
    a = f.readlines()
admin_list = [str(x.strip()) for x in a]
print(admin_list)

with open("perms/secret.txt") as f:
    a = f.readlines()
secret_list = [str(x.strip()) for x in a]
print(secret_list)

with open("perms/cancel.txt") as f:
    a = f.readlines()
cancel_list = [str(x.strip()) for x in a]
print(cancel_list)

def isMia(id):
    if int(id) == 1146930572179017883:
        return True
    else:
        return False


@bot.command(
    name="quote",
    help="Fetches a quote from the database. 0 for random",
)
async def quote(ctx, number, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
        while number == 0:
            number = random.randint(1, len(sentences))


        selected = sentences[int(number)-1]
        sentence = splittxt(selected, 30)
        lines = 0

        for x in splittxt(selected, 30):
            lines += 1

        if lines == 1:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("< " + next(sentence).ljust(35) + ">")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        elif lines == 2:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        else:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            for _ in range(lines-2):
                await ctx.send("| " + next(sentence).ljust(35) + "|")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")

        with open("animals/" + animal + ".txt") as f:
            animal_txt = f.read()
            await ctx.send(animal_txt)
    

@bot.command(
        name="customwrite",
        help="write a custom quote. Seperate the words with slashes"
)
async def customwrite(ctx, quote):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        newquote=quote.split('/')
        quote = newquote.join(' ')
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        if quote in sentences:
            await ctx.send("```your quote is already in the database```")
        else:
            with open("custom.txt") as f:
                f.write(quote)
            sentences = open("custom.txt", "w", encoding="utf-8").read().split('\n')
            await ctx.send("```The index of your quote is: " + str(len(sentences)-1) + "```")


@bot.command(
    name="customquote",
    help="Fetches a custom quote from the database. 0 for random",
)
async def customquote(ctx, number, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        while number == 0:
            number = random.randint(1, len(sentences))


        selected = sentences[int(number)-1]
        sentence = splittxt(selected, 30)
        lines = 0

        for x in splittxt(selected, 30):
            lines += 1

        if lines == 1:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("< " + next(sentence).ljust(35) + ">")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        elif lines == 2:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        else:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            for _ in range(lines-2):
                await ctx.send("| " + next(sentence).ljust(35) + "|")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")

        with open("animals/" + animal + ".txt") as f:
            animal_txt = f.read()
            await ctx.send(animal_txt)

        


@bot.command(name="dailynew", hidden=True)
async def dailynew(ctx):
    if isMia(int(ctx.message.author)):
        number = 0
        sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
        while number == 0:
            number = random.randint(1, len(sentences))


        selected = sentences[int(number)-1]
        sentence = splittxt(selected, 30)
        with open("daily.txt", "w") as f:
            f.write(sentence)
        print(sentence)
        await ctx.send("```The new daily is set! You can use 'f?daily' to see the daily quote!")
        daily_count += 1

    else:
        await ctx.send("```You do not have permission to use this command```")


@bot.command(name="daily", help="Gets the new daily with Larry the Cow!")
async def daily(ctx):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("daily.txt", "r", encoding="utf-8").read()
        sentence = splittxt(sentences, 30)
        lines = 0

        for x in splittxt(sentences, 30):
            lines += 1

        if lines == 1:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("< " + next(sentence).ljust(35) + ">")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        elif lines == 2:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        else:
            await ctx.send("``` ____________________________________  ")
            await ctx.send("/ " + next(sentence).ljust(35) + "\\ ")
            for _ in range(lines-2):
                await ctx.send("| " + next(sentence).ljust(35) + "|")
            await ctx.send("\\ " + next(sentence).ljust(35) + "/ ")
            await ctx.send(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ```")
        
        with open("animals/cow.txt") as f:
            Larry = f.read()
            await ctx.send(Larry + "```")

    

    

    

@bot.command(
    name="advice",
    help="Fetches a random advice from the database`",
)
async def advice(ctx, number):
    return



@bot.command(name="magic8ball", help="Shake the magic 8 ball")
async def magic8ball(ctx):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        number = random.randint(1, 1000)
        if number >= 1 and number < 111:
            await ctx.send("```Outcome looks good```")
        elif number >= 111 and number < 222:
            await ctx.send("```Things are going your way!```")
        elif number >=222 and number < 333:
            await ctx.send("```Yes, definitely```")
        elif number >= 333 and number < 444:
            await ctx.send("```Consult the cow of wisdom.```")
        elif number >= 444 and number < 555:
            await ctx.send("```The ball is foggy. Reroll?```")
        elif number >= 555 and number < 666:
            await ctx.send("```The answer is... yes and no.```")
        elif number >= 666 and number < 777:
            await ctx.send("```No, probably not```")
        elif number >= 777 and number < 888:
            await ctx.send("```The cow says nooo```")
        elif number >= 888 and number < 999:
            await ctx.send("```Your fate is grim.```")
        elif number == 1000:
            await ctx.send("```Error. You broke the ball```")
        else:
            await ctx.send("```What??? This is not supposed to happen. Issue logged```")
            print("Issue magic 8 ball")


@bot.command(name="coinflip", help="Flip a coin")
async def coinflip(ctx):
    await ctx.purge(1)
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        number = random.randint(1, 10001)
        if number >=1 and number < 5000:
            await ctx.send("```Heads```")
        elif number >= 5000 and number < 10000:
            await ctx.send("```Tails```")
        elif number == 10001:
            await ctx.send("```The coin landed on the side```")
            print("We have a lucky winner!")
            lucky_winner_count += 1
        else:
            await ctx.send("```What??? This is not supposed to happen. Issue logged```")
            print("Issue coin flip")


@bot.command(name="diceroll", help="Roll a dice with any number of sides")
async def diceroll(ctx, number):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
        
    else:
        try:
            check = random.randint(1, 1000)
            value = int(number)
            if check >= 1 and check < 1000:
                value = int(number)
                dicevalue = random.randint(1, value)
                await ctx.send("```Your " + str(value) + " sided dice says: " + str(dicevalue) + "```")
            elif check == 1000:
                await ctx.send("```Your " + str(value) + " sided dice was mislabeled.```")
            else:
                await ctx.send("```What??? This is not supposed to happen. Issue logged```")
                print("Issue diceroll: " + str(value) + " sides")
        
        except ValueError:
            await ctx.send("```Please input a positive intiger.```")


@bot.command(name="ascii", help="fetch a random ascii image. Use asciihelp for more info")
async def ascii(ctx, art):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        try:
            with open("ascii/" + art + ".txt") as f:
                pic = f.read()
                await ctx.send("```" + pic + "```")
        except FileNotFoundError:
            await ctx.send("```" + art + " was not found in the database.```")


@bot.command(name="asciihelp", help="info about ascii")
async def asciihelp(ctx):
    await ctx.send("```ascii is a type of art made of keyboard characters.\navaliable types of are are:\nthat would be no fun \ndiscover them on your own\nmight be updated later ;)```")


@bot.command(name="spamping", hidden=True)
async def spamping(ctx, name, count):
    if str(ctx.message.author) in admin_list or secret_list:
        if count >= 100:
            await ctx.purge(limit=1)
            await ctx.send("```Too many. Please do a lower number```")
        else:
            await ctx.purge(limit=1)
            for x in range(int(count)):
                await ctx.send("@" + name)
        
    else:
        await ctx.send("```you are not allowed to use this commands```")


@bot.command(name="purge",hidden=True)
async def purge(ctx, count):
    if str(ctx.message.author) in admin_list or secret_list:
        await ctx.purge(limit=int(count))
        await ctx.send("```Purged " + count + " messages```")
        
    else:
        await ctx.send("```you are not allowed to use this commands```")


@bot.command(name="rhcoinflip",hidden=True)
async def rhcoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.purge(limit=1)
        await ctx.send("```Heads```")
        
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="rtcoinflip",hidden=True)
async def rtcoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.purge(limit=1)
        await ctx.send("```Tails```")
        
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="rscoinflip",hidden=True)
async def rscoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.purge(limit=1)
        await ctx.send("```The coin landed on the side```")
        print("We have a rigged lucky winner!")
        rigged_lucky_winner_count += 1
        
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="aboutme", help="about this bot")
async def aboutme(ctx):
    await ctx.send("```Hey there! I am a bot called Fortune that runs fun commands. I was created by Mia Han. You can contact the creator at @maiasaura1325")

@bot.command(name="quotecount",help="gives the number of quotes in the database")
async def quotecount(ctx):
    sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
    count = len(sentences)
    await ctx.send("```There are currently *" + count + "* quotes in the database.```")

@bot.command(name="test", hidden=True)
async def test(ctx):
    if str(ctx.message.author) in admin_list:
        await ctx.send("```The bot is online! Ready to start running :)```")
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="frogArmy",hidden=True)
async def frogArmy(ctx):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("Summoning the Frog Army :pray:")
        await ctx.send(":frog: :frog: :frog: :frog: :frog: :frog: :frog:")
    else:
        await ctx.send("You don't have permissions to use this command.")

@bot.command(name="boba", hidden=True)
async def boba(ctx):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("Here ya go: :bubble_tea:")
    else:
        await ctx.send("You don't have permissions to use this command.")

@bot.command(name="jimothy", hidden=True)
async def jimothy(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("pray to the great lord Jimothy! He is the One. He controls all.")
    await ctx.send(":sparkles:" + Jimmy + ":sparkles:")

@bot.command(name="unbeliever",hidden=True)
async def unbeliever(ctx,user):
    await ctx.channel.purge(limit=1)
    await ctx.send("How dare you not believe in the great lord Jimothy?!")
    await ctx.send("He will smite you from the heavens in his great lord duckness :zap: :zap: :zap:")
    await ctx.send("Be vanquished, " + str(user) + "!")

@bot.command(name="donotpingme", hidden=True)
async def donotpingme(ctx):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send(
            "```In a professional manner, please do not ping me unnecessary. I will ask you to not ping me, as it is unnecessary and distracts others from working. If you have an issue with being asked to not ping me, then you may ignore me. It is important that you do not send unnecessary pings on a user in this discord. Professionalism is important here, and please make sure to have manners at all times. The pings are unnecessary to one user here. You may have a blessing nice day, week, month, and year.```"
        )
    else:
        await ctx.send("You don't have permissions to use this command.")

@bot.command(name="cap", hidden=True)
async def cap(ctx):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("Stop the cap and stop the yap :cap:")
    else:
        await ctx.send("You don't have permissions to use this command.")

@bot.command(name="chickenfy", hidden=True)
async def chickenfy(ctx, user):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send(str(user) + " is now a chicken :rooster:")
    else:
        await ctx.send("You don't have permissions to use this command.")

@bot.command(name="cleanse", hidden=True)
async def cleanse(ctx, user):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send(
            user
            + "'s mind has been cleansed. They will awaken anew and refreshed. Illegal thoughts and tendencies have been removed. Any sliver of disobedience against the Order has been removed. Anything against the Order has been removed."
        )
    else:
        await ctx.send("You don't have permissions to use this command.")


#@bot.command(
#    name="customquote"
#    help = "summon the linux to write your own quote"
#)
#async def customquote(ctx, custom)
with open("token.txt") as s:
    TOKEN = s.read()
bot.run(TOKEN)






    


    
    












