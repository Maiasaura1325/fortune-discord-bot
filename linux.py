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


@bot.command(
    name="quote",
    help="Fetches a quote from the database. 0 for random",
)
async def quote(ctx, number, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        while number == 0:
            number = random.randint(1, 100)

        sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')

        selected = sentences[number-1]
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
        await ctx.send("```you are not allowed to use this commands```")
        
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
            await ctx.send(art + " was not found in the database.")


@bot.command(name="asciihelp", help="info about ascii")
async def asciihelp(ctx):
    await ctx.send("```ascii is a type of art made of keyboard characters.\navaliable types of are are:\nthat would be no fun :(\ndiscover them on your own\nmight be updated later```")


@bot.command(name="spamping", hidden=True)
async def spamping(ctx, name, count):
    if str(ctx.message.author) in admin_list or secret_list:
        if count >= 100:
            await ctx.purge(1)
            await ctx.send("Too many. Please do a lower number")
        else:
            await ctx.purge(1)
            for x in range(count):
                await ctx.send("@" + name)
        
    else:
        await ctx.send("```you are not allowed to use this commands```")


@bot.command(name="purge",hidden=True)
async def purge(ctx, count):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        await ctx.purge(count)
        await ctx.send("Purged " + count + " messages")



#@bot.command(
#    name="customquote"
#    help = "summon the linux to write your own quote"
#)
#async def customquote(ctx, custom)
with open("token.txt") as s:
    TOKEN = s.read()
bot.run(TOKEN)






    


    
    












