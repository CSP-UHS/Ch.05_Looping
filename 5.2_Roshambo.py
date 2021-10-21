'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Quit")

wins = 0
losses = 0
ties = 0
gameOver = False
while not gameOver:
    comp = random.randint(1, 3)
    user_input = int(input("Please choose 1 for rock, 2 for paper, 3 for scissors and 4 for quit: "))


#User chooses rock
    if user_input==1:
        if comp == user_input:
            print("You both chose rock")
            print("It is a tie!")
            ties+=1
        elif comp == 2:
            print("The computer chose paper and you chose rock")
            print("You Lost!")
            losses+=1
        else:
            print("The computer chose scissors and you chose rock")
            print("You Won!")
            wins+=1


#User chooses paper
    elif user_input==2:
        if comp == user_input:
            print("You both chose paper!")
            print("It is a tie!")
            ties+=1
        elif comp == 3:
            print("The computer chose scissors and you chose paper")
            print("You Lost!")
            losses+=1
        else:
            print("The computer chose rock and you chose paper!")
            print("You Won!")
            wins+=1

#User chooses scissors
    elif user_input==3:
        if comp == user_input:
            print("You both chose scissors")
            print("It is a tie!")
            ties+=1
        elif comp == 2:
            print("The computer chose paper and you chose scissors")
            print("You Won!")
            wins+=1
        else:
            print("The computer chose Rock and you chose scissors")
            print("You Lost!")
            losses+=1

#User quits
    elif user_input==4:
        gameOver=True

#User enters incorrectly
    else:
        print("You entered incorrectly. Try again")


#User has quit and game is over. Print results!
print("Thank you for playing!", "Wins:" , wins, "Losses:", losses,"Ties:", ties)














