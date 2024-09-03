import random;

commandlist = ["help", "stop", "aristo"]
cont = input("Encode?")


def encode_letters():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encoded_set = []
    for x in range(26):
        selected = random.randint(1,(27-x))
        encoded_set.append(letters[selected-2])
        letters.remove(letters[selected-2])
    return encoded_set
        

while cont != "stop":
    if cont == "help":
        print("List of commands: ")
    elif cont == "aristo":
        encoded_set = encode_letters()
        sentence = input("What sentence(s) would you like to encode?")
        sentence_array=[]
        sentence_array.append(c for c in sentence if c.isalpha())
        [x.lower() for x in sentence_array]
        print(sentence_array)

        print("Your encoded set is: ")
        print(encoded_set)
    cont = input("Encode?")