import logging
import sympy
import os
import random
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




def customwrite(quote):
    newquote=quote.split('/')
    quote = ' '.join(newquote)
    sentences = open("customdb.txt", "r", encoding="utf-8").read().split('\n')
    if quote in sentences:
        print(quote + " is already in the database")
    else:
        with open("customdb.txt", "a") as f:
            f.write(quote)
            f.write("\n")
            f.close
        sentences = open("customdb.txt", "r", encoding="utf-8").read().split('\n')
        print("The index of your quote is: " + str(len(sentences)-1) + "")



def customquote(number, animal):
    
    sentences = open("customdb.txt", "r", encoding="utf-8").read().split('\n')
    while number == 0:
        number = random.randint(1, len(sentences))


    selected = sentences[int(number)-1]
    sentence = splittxt(selected, 30)
    lines = 0

    for x in splittxt(selected, 30):
        lines += 1

    if lines == 1:
        print(" ____________________________________  ")
        print("< " + next(sentence).ljust(35) + ">")
        print(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
    elif lines == 2:
        print(" ____________________________________  ")
        print("/ " + next(sentence).ljust(35) + "\\ ")
        print("\\ " + next(sentence).ljust(35) + "/ ")
        print(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
    else:
        print(" ____________________________________  ")
        print("/ " + next(sentence).ljust(35) + "\\ ")
        for _ in range(lines-2):
            print("| " + next(sentence).ljust(35) + "|")
        print("\\ " + next(sentence).ljust(35) + "/ ")
        print(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")

    with open("animals/" + animal + ".txt") as f:
        animal_txt = f.read()
        print(animal_txt)


write_custom = input("Write a custom? ")
while write_custom != "no":
    thing = input(":")
    customwrite(thing)
    write_custom = input("Write a custom? ")

custom_quote = input("Get a custom quote? ")
while custom_quote != "no":
    number = input("What number? ")
    animal = input("What animal? ")
    customquote(number, animal)
    custom_quote = input("Get a custom quote? ")

