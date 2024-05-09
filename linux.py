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
bot = commands.Bot(command_prefix="r!", intents=intents)


def splittxt(text, len):
    sentences = (sentence + ". "
                 for sentence in text.split(". "))
    current_line = ""
    for sentence in sentences:
        if len(current_line >= len):
            yield current_line
            current_line = sentence
        else:
            current_line += sentence
    yield current_line



@bot.command(
    name="quote",
    help="Fetches a quote from the database. -1 for random",
)
async def quote(ctx, number, animal):
    if number == (0-1):
        number = random.randint(1,100)
    
    sentences = []
    with open('quotes.txt'.format(i)) as f:
        sentences += re.findall(r".*?[\.\!\?]+", f.read())
    
    selected = sentences[number-1]
    sentence = splittxt(selected)
    lines = 0
    
    for x in splittxt(selected):
        lines += 1
    
    if lines == 1:
        print("------------------")
        print("< " + next(sentence) + ">")
        print("------------------")
    elif lines == 2:
        print("---------------------------")
        print("/ " + next(sentence) + " \\")
        print("\\ " + next(sentence) + " /")
    else:
        print("---------------------------")
        print("/ " + next(sentence) + " \\")
        for x in (lines-2):
            print("| " + next(sentence) + " |")
        print("\\ " + next(sentence) + " /")
    
    area = ctx.message.channel
    with open("animals/" + animal + ".txt") as f:
        animal = f
        print(f)
    
    
    


    

@bot.command(
    name="advice",
    help="Fetches a random advice from the database`",
)
async def advice(ctx, number):
    if number == 0:
        number = random.randint(1,100)
    
    sentences = []
    with open('advice.txt'.format(i)) as f:
        sentences += re.findall(r".*?[\.\!\?]+", f.read())
    
    selected = sentences[number]
    return selected


@bot.command(
    name="customquote"
    help = "summon the linux to write your own quote"
)
async def customquote(ctx, custom)






    


    
    












