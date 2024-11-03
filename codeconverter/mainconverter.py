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

def caeser():
    encoded_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    shift = random.randint(1,25)
    for x in range(shift):
        temp = encoded_set[-1]
        encoded_set.remove(temp)
        encoded_set.insert(0,temp)
    return encoded_set
    

def filters(characters):
    if (characters in alphabet) or (characters in allowed):
        return True
    else:
        return False

def encode(encoded_set):
    sentence = input("What sentence(s) would you like to encode?\n")
    new_sentence=sentence
    new_sentence = new_sentence.lower()
    sentence_array=list(new_sentence)
    new_sentence = []
    for char in filter(filters, sentence_array):
        new_sentence.append(char)
    
    for x in range(len(encoded_set)):
        for y in range(len(new_sentence)):
            if alphabet[x]==new_sentence[y]:
                new_sentence[y]=encoded_set[x].upper()
    
    print("##################################")
    print("Your encoded sentence is: ")
    print("".join(new_sentence))
    print("Your encoded set is: ")
    print("|".join(encoded_set))
    print("|".join(alphabet))
    print("Your original sentence was: ")
    print("".join(sentence_array).upper())

while cont != "stop":
    if cont == "help":
        print("List of commands: ")
    elif cont == "aristo":
        enlisted = encode_letters()
        encode(enlisted)
    elif cont == "caeser":
        enlisted = caeser()
        encode(enlisted)
    cont = input("Encode?\n")
