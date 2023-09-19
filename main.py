import random
import time

#letting you choose which way around you play
###Bear in mind, option 2 will go on forever. To end it simply just kill the program
typeofgame = input("Would you like to 1. guess the enemy player's number, or 2. the enemy player guess your number? ")

if typeofgame == "1":

    while True:
        
        #generating the enemy player's roll
        aiNum = random.randint(1,6)
        print("The enemy player has rolled their die and covers it with their hands. You roll yours...")
        time.sleep(3)

        #generating your roll and revealing it
        yournum = random.randint(1,6)
        print("You rolled a " + str(yournum) + ".")
        time.sleep(2)

        #getting your guess on what they rolled, higher or lower
        print("\n"); guess = input("Enemy player - Did you roll higher or lower than me? ")
        time.sleep(2)

        #checking if your guess was correct then printing the result
        print("The enemy player reveals their roll.")
        if guess == "Higher" or "higher" and yournum > aiNum:
            print("Correct")
            print(aiNum)

        elif guess == "Lower" or "lower" and yournum < aiNum:
            print("Correct")
            print(aiNum)

        elif yournum == aiNum:
            print("Whoops, it's the same.")

        else:
            print("Wrong")

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

            if aiNum < yournum:
                print("correct")
                print(yournum)
            elif aiNum > yournum:
                print("Wrong")
                print(yournum)
        elif aiGuess == 2:
            print("I think you got lower."); print("You reveal your roll.")
            if aiNum > yournum:
                print("correct")
                print(yournum)
            elif aiNum < yournum:
                print("Wrong")
                print(yournum)
        

        #if the roll was the same it would end in a draw
        elif aiNum == yournum:
            if aiGuess == 1:
                print("I think you got higher. You reveal the roll.")
                print("Whoops, it's the same")
            elif aiGuess == 2:
                print("I think you got lower. You reveal the roll.")
                print("Whoops, it's the same")
            

#if you chose anything other than 1 or 2 it wouldn't work
else:
    print("Not valid option. Restart the program and pick either 1 or 2. ")

