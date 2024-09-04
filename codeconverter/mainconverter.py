import random;
commandlist = ["help", "stop", "aristo"]
cont = input("Encode?\n")
global alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
allowed = ["!", " ", "?", ","]


def encode_letters():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encoded_set = []  
    for x in range(26):
        selected = random.randint(1,(27-x))
        if selected == 1:    
            encoded_set.append(letters[selected-1])
            letters.remove(letters[selected-1])
        else:
            encoded_set.append(letters[selected-2])
            letters.remove(letters[selected-2])
        
    return encoded_set

def filters(characters):
    if (characters in alphabet) or (characters in allowed):
        return True
    else:
        return False




while cont != "stop":
    if cont == "help":
        print("List of commands: ")
    elif cont == "aristo":
        encoded_set = encode_letters()
        sentence = input("What sentence(s) would you like to encode?\n")
        new_sentence=sentence
        new_sentence.lower()
        sentence_array=list(new_sentence)
        new_sentence = []
        for char in filter(filters, sentence_array):
            new_sentence.append(char)


        print(sentence_array)
        print(new_sentence)
        

        print("Your encoded set is: ")
        print(encoded_set)
    cont = input("Encode?\n")