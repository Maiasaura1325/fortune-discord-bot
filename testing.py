import asyncio
import logging
import sympy
import os
import random
import discord
from discord.ext import commands
import re
from random import sample

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

number = int(input("Enter a random number: ")) 
animal = input("Enter a random animal: ")
if number == -1:
    number = random.randint(1, 100)

sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')

selected = sentences[number-1]
sentence = splittxt(selected, 30)
lines = 0

for x in splittxt(selected, 30):
    lines += 1

if lines == 1:
    print(" ____________________________ ")
    print("< " + next(sentence) + ">")
    print(" ____________________________ ")
elif lines == 2:
    print(" ____________________________ ")
    print(" / " + next(sentence) + " \\ ")
    print(" \\ " + next(sentence) + "/ ")
    print(" ____________________________ ")
else:
    print(" ____________________________ ")
    print(" / " + next(sentence) + " \\ ")
    for _ in range(lines-2):
        print("| " + next(sentence) + " |")
    print(" \\ " + next(sentence) + "/ ")
    print(" ____________________________ ")

with open("animals/" + animal + ".txt") as f:
    animal_txt = f.read()
    print(animal_txt)