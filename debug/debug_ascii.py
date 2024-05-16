art = input("What art? ")
while art != "stop":
    try:
        with open("ascii/" + art + ".txt") as f:
            pic = f.read()
            print(pic)
    except FileNotFoundError:
        print(art + " was not found in the database.")
    art = input("What art? ")