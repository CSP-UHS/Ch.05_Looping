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
player=0
computer=0
done=False

while done==False:
    again = True
    print()
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.quit")
    y=int(input("type 1,2,3,or 4:"))
    print()
    if y==1:
        print("Rock")
    elif y==2:
        print("Paper")
    elif y==3:
        print("Scissors")
    else:
        done=True
        again=False

    while again==True:
        print("Vs.")

        x=random.randint(1,3)
        if x==1:
            print("Rock")
        elif x==2:
            print("Paper")
        else:
            print("Scissors")

        print()

        if x==y:
            print("Tie")
        elif x==1 and y==2:
            print("You win")
            player+=1
        elif x==1 and y==3:
            print("The computer wins")
            computer+=1
        elif x==2 and y==1:
            print("The computer wins")
            computer+=1
        elif x==2 and y==3:
            print("You win")
            player+=1
        elif x==3 and y==1:
            print("You win")
            player+=1
        elif x==3 and y==2:
            print("The computer wins")
            computer+=1
        again=False
        print()
        print("Your current score is, ",computer,"computer",player,"player")


print("Your final score is, ", computer, "computer", player, "player")
print("Your win rate is",(player/(player+computer))*100,"%")
print("Thank you for playing")

