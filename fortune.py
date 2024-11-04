import asyncio
import logging
import sympy
import os
import random
import discord
from discord.ext import commands
import re
import traceback
from random import sample

#use @bot.tree.command for slash commands 



intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="f?", intents=intents)
global lucky_winner_count, rigged_lucky_winner_count
lucky_winner_count = 0
rigged_lucky_wnner_count = 0
daily_count = 0

@bot.event
async def on_ready():
    print("The bot is online! Ready to start yapping!")
    print(f"Logged in as {bot.user}!")

    guild_id = 1199168199338508449
    guild = discord.Object(id=guild_id)

    await bot.tree.sync(guild=guild)
    print("Slash commands synced!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found!")
    else:
        print(f"An error occured: {error}")
        traceback.print_exc()


#EMOJIS
Jimmy = '<:jimothy:1302815231252369419>'


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
def format_quote(selected, animal):
    sentence = splittxt(selected, 35)
    quoteline = ["``` ______________________________________  "]
    lines = list(sentence)

    if len(lines) == 1:
        quoteline.extend(["< " + lines[0].ljust(37) + ">", " " + "‾" * 37 + " "])
    elif len(lines) == 2:
        quoteline.extend(["/ " + lines[0].ljust(37) + "\\ ", "\\ " + lines[1].ljust(37) + "/ ", " " + "‾" * 37 + " "])
    else:
        quoteline.extend(["/ " + lines[0].ljust(37) + "\\ "] +
                         ["| " + line.ljust(37) + "|" for line in lines[1:-1]] +
                         ["\\ " + lines[-1].ljust(37) + "/ ", " " + "‾" * 37 + " "])
    try:
        with open(f"animals/{animal}.txt") as f:
            animal_txt = f.read()
            quoteline.append(animal_txt + "```")
    except FileNotFoundError:
        quoteline = [f"```'{animal}' was not found in the database. Try checking the spelling or capitalization.```"]

    return "\n".join(quoteline)

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
    help="Fetches a quote from the database. 0 for random"
)
async def quote(ctx, number:int, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
        
    else:
        sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
        if number > len(sentences):
            await ctx.send("```The quote index[" + str(number) + "] was not found.```")
        else:
            while number == 0:
                number = random.randint(1, len(sentences))


            selected = sentences[int(number)-1]
            truequote=format_quote(selected, animal)
            await ctx.send(truequote)
@bot.tree.command(
    name = "quote",
    description = "Fetches a quote from the database. 0 for random"
)     
async def quote(ctx: discord.Interaction, number:int, animal:str):
    if str(ctx.user) in cancel_list:
        await ctx.response.send_message("```you are not allowed to use this command```")
    else:
        sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
        if number > len(sentences):
            await ctx.response.send_message("```The quote index[" + str(number) + "] was not found.```")
        else:
            while number ==0:
                number = random.randint(1,len(sentences))
            selected = sentences[int(number)-1]
            truequote = format_quote(selected, animal)
            await ctx.response.send_message(truequote)
   

@bot.command(
        name="customwrite",
        help="write a custom quote. Seperate the words with slashes"
)
async def customwrite(ctx, *, quote:str):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
        
    else:
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        if quote in sentences:
            await ctx.send("```your quote is already in the database```")
        else:
            with open("custom.txt", "a") as f:
                f.write(quote)
                f.write("\n")
                f.close
            sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
            await ctx.send("```The index of your quote is: " + str(len(sentences)-1) + "```")
@bot.tree.command(
        name = "customwrite",
        description = "write a custom quote. no need for slash seperation"
)
async def customwrite(ctx: discord.Interaction, quote:str):
    if str(ctx.user) in cancel_list:
        await ctx.response.send_message("```you are not allowed to use this command```")
    else:
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        if quote in sentences:
            await ctx.response.send_message("```your quote is already in the database```")
        else:
            with open("custom.txt", "a") as f:
                f.write(quote)
                f.write("\n")
                f.close
            sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
            await ctx.response.send_message("```The index of your quote is: " + str(len(sentences)-1) + "```")
        


@bot.command(
    name="customquote",
    help="Fetches a custom quote from the database. 0 for random"
)
async def customquote(ctx, number:int, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
        
    else:
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        if number > len(sentences):
            await ctx.send("```The quote index[" + str(number) + "] was not found.```")
        else:
            while number == 0:
                number = random.randint(1, len(sentences))


            selected = sentences[int(number)-1]
            truequote = format_quote(selected, animal)
            await ctx.send(truequote)
@bot.tree.command(
        name = "customquote",
        description = "Fetches a custom quote from the databse. 0 for random"
)
async def customquote(ctx:discord.Interaction, number:int, animal:str):
    if str(ctx.message.author) in cancel_list:
        await ctx.response.send_message("```you are not allowed to use this command```")
    else:
        sentences = open("custom.txt", "r", encoding="utf-8").read().split('\n')
        if number > len(sentences):
            await ctx.response.send_message("```The quote index[" + str(number) + "] was not found.```")
        else:
            while number == 0:
                number = random.randint(1, len(sentences))


            selected = sentences[int(number)-1]
            truequote = format_quote(selected, animal)
            await ctx.response.send_message(truequote)

@bot.command(name="dailynew", hidden=True)
async def dailynew(ctx, message):
    if isMia(int(ctx.message.author)):
        if message == "random":    
            number = 0
            sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
            while number==0:
                number = random.randint(1,len(sentences))
            selected = sentences[int(number)-1]
            with open("daily.txt", "w") as f:
                f.write(str(selected))
        else:
            newquote=message.split('/')
            message = newquote.join(' ')
            with open("daily.txt", "w") as f:
                f.write(message)
        await ctx.send("```The new daily is set! You can use 'f?dailylarry' or 'f?dailyelon' to see the daily quote!```")

    else:
        await ctx.send("```You do not have permission to use this command```")
@bot.tree.command(name="dailynew", description="Get new daily. Only owner permitted")
async def dailynew(ctx:discord.Interaction, message:str):
    if isMia(int(ctx.user)):
        if message == "random":    
            number = 0
            sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
            while number==0:
                number = random.randint(1,len(sentences))
            selected = sentences[int(number)-1]
            with open("daily.txt", "w") as f:
                f.write(str(selected))
        else:
            with open("daily.txt", "w") as f:
                f.write(message)
        await ctx.response.send_message("```The new daily is set! You can use '/dailylarry' or '/dailyelon' to see the daily quote!```")
            
    else:
        await ctx.response.send_message("```You do not have permission to use this command```")


@bot.command(name="dailylarry", help="Gets the new daily with Larry the Cow!")
async def dailylarry(ctx):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("daily.txt", "r", encoding="utf-8").read()
        quote = format_quote(sentences, "cow")
        await ctx.send(quote)
@bot.tree.command(name="dailylarry", description="Gets the new daily with Larry the Cow!")
async def dailylarry(ctx: discord.Interaction):
    if str(ctx.user) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("daily.txt", "r", encoding="utf-8").read()
        quote = format_quote(sentences, "cow")
        await ctx.response.send_message(quote)


@bot.command(name="dailyelon", help="Gets the new daily with Elon the Bird!")
async def dailyelon(ctx):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("daily.txt", "r", encoding="utf-8").read()
        quote = format_quote(sentences, "bird")
        await ctx.send(quote)
@bot.tree.command(name="dailyelon", description="Gets the new daily with Elon the Bird!")
async def daily(ctx: discord.Interaction):
    if str(ctx.user) in cancel_list:
        await ctx.send("```you are not allowed to use this commands```")
        
    else:
        sentences = open("daily.txt", "r", encoding="utf-8").read()
        quote = format_quote(sentences, "bird")
        await ctx.response.send_message(quote)
    
'''@bot.command(
    name="submitadvice",
    help="Submit a piece of advice; it can be verified to be put in the advice database. Seperate words with '/'."
)
async def submitadvice(ctx, advice):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
    else:
        newquote=advicequote.split('/')
        advicequote = newquote.join(' ')
        sentences = open("advice.txt", "r", encoding="utf-8").read().split('\n')
        verify_person_id=1146930572179017883
        verify_person = await bot.fetch_user(verify_person_id)
        if advicequote in sentences:
            await ctx.send("```your advice is already in the database```")
        else:
            try:
                message = await verify_person.send(f"Advice from {ctx.author.name} (ID: {ctx.author.id}): {advicequote}")
                await message.add_reaction('✅')
                await message.add_reaction('❌')
                advicequote[message.id]= (advicequote, ctx.author)
                await ctx.send("```your advice has been submitted and will be verified within 72 hours!```")
            except Exception:
                await ctx.send("```your advice could not be submitted```")

@bot.event
async def on_reaction_add(reaction, user):
    verify_person_id=1146930572179017883
    if user.id==verify_person_id and reaction.message.id in advice:
        if reaction.emoji=='✅':
            pass
        elif reaction.emoji=='❌':
            pass'''


'''@bot.command(
    name="advice",
    help="Fetches a random advice from the database`",
)
async def advice(ctx, number, animal):
    if str(ctx.message.author) in cancel_list:
        await ctx.send("```you are not allowed to use this command```")
        
    else:
        sentences = open("advice.txt", "r", encoding="utf-8").read().split('\n')
        if number > len(sentences):
            await ctx.send("```The advice index[" + str(number) + "] was not found.```")
        else:
            while number == 0:
                number = random.randint(1, len(sentences))


            selected = sentences[int(number)-1]
            sentence = splittxt(selected, 30)
            lines = 0

            for x in splittxt(selected, 30):
                lines += 1

            quoteline=[]
            if lines == 1:
                quoteline.append("``` ____________________________________  ")
                quoteline.append("< " + next(sentence).ljust(35) + ">")
                quoteline.append(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
            elif lines == 2:
                quoteline.append("``` ____________________________________  ")
                quoteline.append("/ " + next(sentence).ljust(35) + "\\ ")
                quoteline.append("\\ " + next(sentence).ljust(35) + "/ ")
                quoteline.append(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
            else:
                quoteline.append("``` ____________________________________  ")
                quoteline.append("/ " + next(sentence).ljust(35) + "\\ ")
                for _ in range(lines-2):
                    quoteline.append("| " + next(sentence).ljust(35) + "|")
                quoteline.append("\\ " + next(sentence).ljust(35) + "/ ")
                quoteline.append(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")

            try:
                with open("animals/" + animal + ".txt") as f:
                    animal_txt = f.read()
                    quoteline.append(animal_txt + "```")
            except FileNotFoundError:
                quoteline=["```'" + animal + "' was not found in the database. Try checking the spelling or capitalization.```"]
            
            truequote="\n".join(quoteline)
            await ctx.send(truequote)
'''

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
    await ctx.channel.purge(limit=1)
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
            #lucky_winner_count += 1
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
async def spamping(ctx, user: discord.Member, count:int):
    if str(ctx.message.author) in admin_list or secret_list:
        if count >= 100:
            await ctx.channel.purge(limit=1)
            await ctx.send("```Too many. Please do a lower number```")
        else:
            await ctx.channel.purge(limit=1)
            for x in range(int(count)):
                await ctx.send(f"{user.mention}")
        
    else:
        await ctx.send("```you are not allowed to use this commands```")


@bot.command(name="purge",hidden=True)
async def purge(ctx, count:int):
    if str(ctx.message.author) in admin_list or secret_list:
        await ctx.channel.purge(limit=int(count))
        await ctx.send("```Purged " + count + " messages```")
        
    else:
        await ctx.send("```you are not allowed to use this commands```")


#Write a command that edits the user's message and replaces it with f?coinflip
@bot.command(name="rhcoinflip",hidden=True)
async def rhcoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("```Heads```")
        
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="rtcoinflip",hidden=True)
async def rtcoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("```Tails```")
        
    else:
        await ctx.send("```You do not have the permission to use this command.```")

@bot.command(name="rscoinflip",hidden=True)
async def rscoinflip(ctx):
    if str(ctx.message.author) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("```The coin landed on the side```")
        print("We have a rigged lucky winner!")
        #rigged_lucky_winner_count += 1
        
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

@bot.command(name="frogarmy",hidden=True)
async def frogArmy(ctx):
    if str(ctx.message.author.id) in secret_list:
        await ctx.channel.purge(limit=1)
        await ctx.send("Summoning the Frog Army :pray:")
        await ctx.send(":frog: :frog: :frog: :frog: :frog: :frog: :frog:🐸")
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
        await ctx.send("Stop the cap and stop the yap :billed_cap:")
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

@bot.command(name="bluegummi", hidden=True)
async def bluegummi(ctx):
    if isMia(str(ctx.message.author.id)):
        await ctx.send("```bluegummi this is your fault that I made it I will blame you and larry the cow for this 6 month cowsay obsession.```")
    elif str(ctx.message.author.id)== 710548131992961074:
        await ctx.send("@bluegummi this is your fault I made this bot I will blame it on you and larry the cow for this 3 moth ascii and cowsay obsession")         
    else:
        await ctx.send("```You do not have permission to use this command.(Maybe as bluegummi to use it?:))```")


with open("token.txt") as s:
    TOKEN = s.read()
bot.run(TOKEN)






    


    
    












