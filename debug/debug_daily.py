import random


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
daily_count = 0


def dailynew():
    number = 0
    sentences = open("quotes.txt", "r", encoding="utf-8").read().split('\n')
    while number == 0:
        number = random.randint(1, len(sentences))


    selected = sentences[int(number)-1]
    sentence = splittxt(selected, 30)
    with open("daily.txt", "w") as f:
        f.write(str(selected))
    print("The new daily is set! You can use 'f?daily' to see the daily quote!")


def dailycustom(sentence):
    newquote=sentence.split('/')
    quote = ' '.join(newquote)
    
    with open("daily.txt", "w") as f:
        f.write(quote)
        f.close
    print("Your quote has been written.")
    

        



def daily():
    
        
    sentences = open("daily.txt", "r", encoding="utf-8").read()
    sentence = splittxt(sentences, 30)
    lines = 0

    for x in splittxt(sentences, 30):
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
    
    with open("animals/cow.txt") as f:
        Larry = f.read()
        print(Larry)


def dailycount():
    print("Daily count is: " + str(daily_count))


command = input("What command? ")
while command != "stop":
    if command == "dailynew":
        dailynew()
        daily_count += 1
    elif command == "daily":
        daily()
    elif command == "dailycount":
        dailycount()
    elif command == "dailycustom":
        custom = input("What is your sentence? ")
        dailycustom(custom)
    else:
        print("Command not found. Try again?")
    command = input("What command? ")


