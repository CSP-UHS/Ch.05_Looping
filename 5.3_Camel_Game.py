'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random
#Instructions
print("\033[1;31;20mHello, welcome to the camel game ")
print("Here are the instructions")
print("You must ride your camel across the desert to escape the natives")
print("You will have to be accountable for your camel and your thirst levels")
print("You will be able to control the speed you go at, whether or not you want to stop, etc")
print("You must travel 200 miles across the dessert back to your mainland in order to escape the natives")
print("You must be careful in order to keep your camels tiredness below an 8")
print("You also must be careful in order to keep your thirst levels below a 6")
print("Good luck traveler! \n")



#Main loop, variables, and choices
gameOver = False
camel_tired = 0
thirst = 0
native_distance = -20
canteen_drinks = 3
miles = 0
while not gameOver:
    print()
    print("\033[1;37;20mA. Drink from canteen. ")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")
    print()


    user_input = input("What is your choice? ")

    #oasis section
    oasis = random.randint(1,20)
    if oasis == 1:
        print()
        print("You have found an oasis!")
        print()
        camel_tired = 0
        thirst = 0
        canteen_drinks = 3

    # if camels tired levels get above a 5 print they are tired
    # if camels tired levels get above 8 print that your camel has died and end the game
    if camel_tired == 5:
        print("Your camel is tired!")
    elif camel_tired > 9:
        print("You idiot! you killed your camel")
        gameOver = True
        print("Good try young traveler, you did well on your journey")
        break

    # if thirst levels are above 4 print that they are thirsty
    # if thirst levels are above 6 print they have died and end the game
    if thirst == 4:
        print("You are thirsty")
    if thirst > 6:
        print("You idiot! You have died of thirst!")
        gameOver = True
        print("Good try young traveler, you did well on your journey")
        break

    # if natives catch up to them then print they were killed and end game
    if native_distance == 15:
        print("The natives are close behind!")
    elif native_distance >= miles:
        print("The natives have caught you")
        gameOver = True
        print("Good try young traveler, you did well on your journey")
        break



    # if user drinks from canteen
    if user_input.upper() == "A":
        print()
        print("You drink from your canteen")
        print()
        canteen_drinks-=1
        thirst = 0
     # If user chooses full speed
    elif user_input.upper() == "C":
        native_miles = random.randint(7, 10)
        native_distance += native_miles
        full = random.randint(13,21)
        miles+=full
        camel_tired+=3
        thirst+=1
        print()
        print("You choose to go full speed ahead")
        print("You have gone a total of", full,"miles")
        print("The natives are",miles-native_distance,"behind you")
        print()
    # If user chooses moderate speed
    elif user_input.upper() == "B":
        native_miles = random.randint(7, 10)
        native_distance += native_miles
        moderate = random.randint(5, 12)
        miles += moderate
        camel_tired+=1
        thirst+=1
        print()
        print("You decide to go at a moderate pace")
        print("You have gone a total of", moderate,"miles")
        print("The natives are", miles-native_distance,"miles behind you")
        print()
    # If user stops for night
    elif user_input.upper() == "D":
        native_miles = random.randint(7, 10)
        native_distance += native_miles
        camel_tired = 0
        print()
        print("You stop for the night")
        print("The camel is very happy")
        print("The natives are", miles-native_distance,"miles behind")
        print()

     #if user chooses status check
    elif user_input.upper() == "E":
        print("Canteen drinks:", canteen_drinks)
        print("Thirst:", thirst)
        print("Camel tiredness",camel_tired)
        print("Miles traveled:", miles)
        print("The natives are",miles-native_distance,"miles behind")
        print()
    # if user quits
    elif user_input.upper() == "Q":
        gameOver = True
        print()
        print("Pathetic")
        print()
    # If user chooses incorrectly
    else:
        print("Not an option!")



    #if user wins
    if gameOver == False and miles >= 200:
        print()
        print("Good job! You have won the game!")
        print()








