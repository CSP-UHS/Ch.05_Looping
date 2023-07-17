'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
win=0
tie=0
lose=0
games=0
quit = False
while not quit:
    print("You have played ", games, " games so far!")
    print("Choose a Command below")
    command = int(input("1: rock 2: paper 3: scissors 4: quit ==> "))
    if command == 4:
        quit = True
        break
    games+=1

    if command == 3:
        print("You chose scissors!")
    elif command == 2:
        print("You chose paper!")
    else:
        print("You chose rock!")
    num = random.randrange(1,4)
    if num == 1:
        print("The computer chose rock!")
    elif num == 2:
        print("The computer chose paper!")
    else:
        print("The computer chose scissors!")

    if num == command:
        tie+=1
        print("You Tied!")
    elif command == num+1 or num == 3 and command == 1:
        win+=1
        print("You Won!")
    else:
        lose+=1
        print("You Lose!")
        print(num)

if games >= 10:
    print("Thank you for playing 10 or more games of Roshambo!")
else:
    print("You only played ", games, " games! All your ties are going to become losses ")
    lose+=tie
    tie=0
print("You won ", win, " games and tied in ", tie, " games and lost in ", lose, " games!" )












