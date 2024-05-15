import random
lucky_winner_count = 0



command = input("What command? ")
while command != "stop":
    if command == "coinflip":
        number = random.randint(1, 10001)
        if number >=1 and number < 5000:
            print("Heads")
        elif number >= 5000 and number < 10000:
            print("Tails")
        elif number == 10001:
            print("The coin landed on the side")
            print("We have a lucky winner!")
            lucky_winner_count += 1
        else:
            print("What??? This is not supposed to happen. Issue logged")
            print("Issue coin flip")

    elif command == "luckywinnercount":
        print("The lucky winner count is: " + str(lucky_winner_count) + ".")

    elif command == "diceroll":
        number = input("What number of sides? ")
        try:
            check = random.randint(1, 1000)
            value = int(number)
            if check >= 1 and check < 1000:
                dicevalue = random.randint(1, value)
                print("Your " + str(value) + " sided dice says: " + str(dicevalue))
            elif check == 1000:
                print("Your " + str(value) + " sided dice was mislabeled.")
            else:
                print("What??? This is not supposed to happen. Issue logged")
                print("Issue diceroll: " + str(value) + " sides")
        
        except ValueError:
            print("Please input a positive intiger.")

    elif command == "magic8ball":
        number = random.randint(1, 1000)
        if number >= 1 and number < 111:
            print("Outcome looks good")
        elif number >= 111 and number < 222:
            print("Things are going your way!")
        elif number >=222 and number < 333:
            print("Yes, definitely")
        elif number >= 333 and number < 444:
            print("Consult the cow of wisdom.")
        elif number >= 444 and number < 555:
            print("The ball is foggy. Reroll?")
        elif number >= 555 and number < 666:
            print("The answer is... yes and no.")
        elif number >= 666 and number < 777:
            print("No, probably not")
        elif number >= 777 and number < 888:
            print("The cow says nooo")
        elif number >= 888 and number < 999:
            print("Your fate is grim.")
        elif number == 1000:
            print("Error. You broke the ball")
        else:
            print("What??? This is not supposed to happen. Issue logged")
            print("Issue magic 8 ball")
    
    elif command == "coinflipalpha":
        lucky_winner_alpha_count = 0
        heads_count = 0
        tails_count = 0
        for x in range(1000):
            number = random.randint(1, 10001)
            if number >=1 and number < 5000:
                print("Heads")
                heads_count += 1
            elif number >= 5000 and number < 10000:
                print("Tails")
                tails_count += 1
            elif number == 10000 or 10001:
                print("The coin landed on the side")
                print("We have a lucky winner!")
                lucky_winner_count += 1
                lucky_winner_alpha_count +=1
        print("heads: " + str(heads_count))
        print("tails: " + str(tails_count))
        print("lucky winners: " + str(lucky_winner_alpha_count))
    
    elif command == "coinflipbeta":
        lucky_winner_beta_count = 0
        heads_count = 0
        tails_count = 0
        for x in range(10000):
            number = random.randint(1, 10001)
            if number >=1 and number < 5000:
                print("Heads")
                heads_count += 1
            elif number >= 5000 and number < 10000:
                print("Tails")
                tails_count += 1
            elif number == 10001:
                print("The coin landed on the side")
                print("We have a lucky winner!")
                lucky_winner_count += 1
                lucky_winner_beta_count +=1
        print("heads: " + str(heads_count))
        print("tails: " + str(tails_count))
        print("lucky winners: " + str(lucky_winner_beta_count))
    
    command = input("What command? ")
