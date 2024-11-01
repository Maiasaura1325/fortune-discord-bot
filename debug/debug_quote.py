import random
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
genquote = input("Generate a quote? ")
while genquote != "no":
    number = int(input("Enter a random number: ")) 
    animal = input("Enter a random animal: ")
    sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
    if number > len(sentences):
        print("The quote index[" + str(number) + "] was not found.")
        genquote = input("Generate a quote? ")
    else:    
        while number == 0:
            number = random.randint(1, len(sentences))
        


        selected = sentences[number-1]
        sentence = splittxt(selected, 30)
        lines = 0

        for x in splittxt(selected, 30):
            lines += 1

        quoteline=[]
        if lines == 1:
            quoteline.append(" ____________________________________  ")
            quoteline.append("< " + next(sentence).ljust(35) + ">")
            quoteline.append(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
        elif lines == 2:
            quoteline.append(" ____________________________________  ")
            quoteline.append("/ " + next(sentence).ljust(35) + "\\ ")
            quoteline.append("\\ " + next(sentence).ljust(35) + "/ ")
            quoteline.append(" ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅  ")
        else:
            quoteline.append(" ____________________________________  ")
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
        print(truequote)
        
        genquote = input("Generate a quote? ")