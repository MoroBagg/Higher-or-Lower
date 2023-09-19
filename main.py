import random
import time

#letting you choose which way around you play
###Bear in mind, option 2 will go on forever. To end it simply just kill the program
typeofgame = input("Would you like to 1. guess the enemy player's number, or 2. the enemy player guess your number? ")

if typeofgame == "1":

    while True:
        
        #generating the enemy player's roll
        aiNum = random.randint(1,6)
        print("\n")
        print("\n")
        print("The enemy player has rolled their die and covers it with their hands. You roll yours...")
        time.sleep(3)

        #generating your roll and revealing it
        yournum = random.randint(1,6)
        print("You rolled a " + str(yournum) + ".")
        time.sleep(2)

        #getting your guess on what they rolled, higher or lower
        print("\n")
        print("Enemy player: Did you get the higher or lower number? (just say higher or lower)")
        guess = input("You: ")
        time.sleep(2)

        #checking if your guess was correct then printing the result
        print("The enemy player reveals their roll.")
        if (guess == "Higher" or guess == "higher") and yournum > int(aiNum):
            print("Correct"); print("\n")
            print("The enemy player's die had the number " + str(aiNum) + " on it.")

        elif (guess == "Lower" or guess == "lower") and yournum < int(aiNum):
            print("Correct"); print("\n")
            print("The enemy player's die had the number " + str(aiNum) + " on it.")

        elif yournum == int(aiNum):
            print("Whoops, it's the same."); print("\n")
            print("Both die had the number " + str(aiNum) + " on it.")
            

        else:
            print("Wrong")
            print("The enemy player's die had the number  " + str(aiNum) + " on it.")
            
elif typeofgame == "2":

    while True:

        #generating your roll
        yournum = random.randint(1,6)
        print("You roll the die then cover it with your hands. The enemy player rolls theirs...")
        time.sleep(3)

        #generating the enemy player's roll
        aiNum = random.randint(1,6)
        print("The enemy player rolled a " + str(aiNum))
        time.sleep(2)
        print("\n"); print("You - Did you roll higher or lower than me?")

        #using random integer to use as the enemy player's guess for if you got higher or lower than them
        aiGuess = random.randint(1,2)
        time.sleep(2)

        #checking if they were correct
        if aiGuess == 1:
            print("I think you got higher."); print("You reveal your roll.")
            time.sleep(2)

            if aiNum < int(yournum):
                print("correct"); print("\n")
                print("You had the number " + str(yournum) + " on it")
            elif aiNum > int(yournum):
                print("Wrong");print("\n")
                print("You had the number " + str(yournum) + " on it")        
            print("I think you got lower."); print("You reveal your roll.")
        elif aiGuess == 2:
            if aiNum > int(yournum):
                print("correct");print("\n")
                print("You had the number " + str(yournum) + " on it")
            elif aiNum < int(yournum):
                print("Wrong");print("\n")
                print("You had the number " + str(yournum) + " on it")
        

        #if the roll was the same it would end in a draw
        elif aiNum == int(yournum):
            if aiGuess == 1:
                print("I think you got higher. You reveal the roll.");print("\n")
                print("Whoops, it's the same. Both die had the number " + str(yournum) + " on them")
            elif aiGuess == 2:
                print("I think you got lower. You reveal the roll.");print("\n")
                print("Whoops, it's the same. Both die had the number " + str(yournum) + " on them")
            

#if you chose anything other than 1 or 2 it wouldn't work
else:
    print("Not valid option. Restart the program and pick either 1 or 2. ")


