'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random

play=True

while play==True:
    #Variables
    done = False
    won=1
    lost=1
    pmiles=0 #Player miles
    rest=0
    damage=0
    drunk=10
    ccmiles=0 #Cursed Captain miles
    barrels_of_rum=10
    #Variables

    #introduction
    print()
    print("Welcome to The Pirate Game")
    print("You have stolen a large amount of treasure from The Cursed Captain")
    print("You have to travel 200 miles to hide your treasure")
    print("Make sure to monitor your crews sleep and drunkenness")
    print("If your boat sinks or you become sober then you lose")
    print("Make sure you also dont get caught by the Cursed Captain")
    print("Good luck")
    #introduction


    while not done:

        #Choices
        print()
        print("1. Drink rum (+5 drunkenness)")
        print("2. Ahead at lightning speed (+20miles,80% chance of crash)")
        print("3. Ahead at moderate speed (+15miles,50% chance of crash")
        print("4. Ahead at a snails pace (+10miles,20% chance of crash")
        print("5. Anchor for the night (sleep and repair ship)")
        print("6. Status check")
        print("7. Quit")
        user=int(input("What do you choose? "))
        print()
        #Choices

        if user==7: #quit
            done=True


        elif user==6:#Status Check
            print("Your have traveled",pmiles,"miles")
            print("The Cursed Captain is", pmiles - ccmiles, "miles behind you")
            print("You have",barrels_of_rum,"barrels of rum (Dont run out)")
            print("Your crew drunkenness is",drunk,"(Dont let it hit 0)")
            print("Your boats damage is at",damage,"(Dont let it hit 10)")
            print("Your rest is at",rest,"(Dont let it hit 10)")
            continue

        elif user==5: #Sleep
            rest=0
            print("You decided to anchor for the night")
            print("You can take this time to repair your ship but your crew will get less sleep")
            repair=input("Repair yes(-5 damage,-3 sleep) or no(-0 damage,-5 sleep) ")
            if repair=="yes":
                damage-=5
                if damage<0:
                    damage=0
                rest-=3
                if rest<0:
                    rest=0
                if ccmiles>=pmiles:
                    print("The Cursed Captain caught up to you while your crew was asleep")
                    print("He took all of your treasure, killed your crew, and sunk your ship")
                    print("As you watch his ship sail away sharks consume you limb by limb")
                    lost=0
                    break
                else:
                    print("*One day later*")
                    print("The crew is unhappy they had to fix the ship but at least they got some sleep")
            else:
                rest-=5
                print("*One day later*")
                print("The crew is happy and well rested")


        elif user==4: #snails pace
            pmiles+=10
            if pmiles >= 200:
                done=True
                won=0
                break
            chance=random.randint(1,10)
            if chance>=2:
                print("Your drunken crew actually managed to not break the ship")
                print("They must have a great captain ;)")
            else:
                print("Maybe your crew is still a little to drunk to go this fast")
                damage += random.randint(2, 5)
                print("Your damage has grown to", damage, ",don't let it reach 10")
                print("You might want to stop for the night to repair your ship")

        elif user==3: #moderate pace
            pmiles+=15
            if pmiles >= 200:
                done=True
                won=0
                break
            chance=random.randint(1,10)
            if chance>=5:
                print("Your drunken crew actually managed to not break the ship")
                print("They must have a great captain ;)")
            else:
                print("Maybe your crew is still a little to drunk to go this fast")
                damage+=random.randint(2,5)
                print("Your damage has grown to",damage,",don't let it reach 10")
                print("You might want to stop for the night to repair your ship")

        elif user==2: #lightning pace
            pmiles+=20
            if pmiles >= 200:
                done=True
                won=0
                break
            chance=random.randint(1,10)
            if chance>=9:
                print("Your drunken crew actually managed to not break the ship going that fast.")
                print("They must have a great captain ;)")
            else:
                print("Your drunken crew crashed into a rock")
                damage+=random.randint(2,5)
                print("Your damage has grown to",damage,",don't let it reach 10")
                print("You might want to stop for the night to repair your ship")

        elif user==1: #drink rum
            drunk+=5
            barrels_of_rum-=1
            print("One more barrel of rum down")
            print("Your crew is happy")
            continue
        else:
            print("Not an option")
            continue

        drunk-=2
        rest+=2

        # Death
        if drunk == 0:
            lost=0
            print("Your crew is sober")
            print("There was a mutiny")
            print("You died")
            break
        if barrels_of_rum <=0:
            lost=0
            print("You ran out of rum")
            break
        if rest>= 10:
            lost=0
            print("Your crew died from exhaustion")
            break
        if damage>=10:
            lost=0
            print("Your ship sank")
            break
        if pmiles-ccmiles<=0:
            lost=0
            print("The Cursed Captain caught up to you")
            print("He took your gold and killed your crew")
            print("He slowly cut pieces off of you and fed them to sharks")
            print("A very slow and painful death")
            break
        if pmiles >= 200:
            won=1
            break

        ccmiles+=random.randint(7,14)
        if pmiles-ccmiles>0:
            print("The Cursed Captain is", pmiles - ccmiles, "miles behind you")
            print("Don't let him catch you")
        else:
            done=True


    if lost==0:
        print("\033[1;31m You lost\033[m")
    if won==0:
        print("\033[1;32m You won, congratulations captain\033[m")
        print("\033[1;32m You outran the Cursed Captain\033[m")
        print("\033[1;32m You and your crew can now celebrate with all of their treasure\033[m")

    k=input("Do you want to play again (Yes/No): ")
    if k.lower()=="no":
        play=False