'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
win = False
done = False
attack = False
magnet = False
build = False
destroy = False
instructions = False
status = False
supplies = 1
check = False
life = 7
codeParts = 0
robotComm = 100
robotDistance = 50
gas = 100
print()
print("Welcome to the game of Robots!")
print()
print("Would you like instructions?")
print()
choice = int(input("1. Yes 2. No ==> "))
print()
print()
print()
if choice == 1 or choice == 2:
    if choice == 1:
        print("Welcome to the game of Robots!")
        print("The object of the game is to get 6 termination code parts to destroy an AI that is taking over the")
        print("world before you get captured by the Robots and turned into a angry Cyborg.")
        print("You will be asked for commands every once in a while.")
        print()
        print()
        print()
        print("C O M M A N D S :                            I N   G A M E   U N L O C K E D  C O M M A N D S")
        print("1. Use Supplies                              7. Locked")  # Attack Robots for supplies
        print("2. Search at a moderate speed                8. Locked")  # Use magnet
        print("3. Search at full speed                      9. Locked")  # Build Termination code
        print("4. Search for supplies                       10. Locked")  # Destroy the AI
        print("5. Status check                              11. Locked")  # Instructions for Unlocked commands
        print("6. quit                                      12. Locked")  # Unlocked command, Status check
        print()
        print()
        print()
        print("You have one little bag of supplies which will last you 7 commands.")
        print("You can get supplies by searching for supplies and some other ways not found yet.")
        print("Good Luck, And kill alot of Robots!")
        print("You are at your home getting ready for a journey to save the world.")
    else:
        print("Good Luck, And kill alot of Robots!")
        print("You are at your home getting ready for a journey to save the world.")

while not done:
    print()
    print()
    if codeParts > 5:
        build = True
        print("You unlocked the command build the termination code, you need 6 termination code parts and")
        print("30 small bags of supplies to build it.")
    if life < 4:
        print("You are thirsty and hungry.")
    if gas < 31:
        print("Your motorcycle is low on gas you need to find a gas station soon!")
    if robotDistance < 16:
        print("The robots are getting close!")
    if robotComm < 11:
        print("You only have ", robotComm, "commands left to win the game.")
    print()
    print()
    print("C O M M A N D S :                            I N   G A M E   U N L O C K E D  C O M M A N D S")
    if attack:
        print("1. Use Supplies                              7. Attack Robots for supplies")
    else:
        print("1. Use Supplies                              7. Locked")
    if magnet:
        print("2. Search at a moderate speed                8. Use magnet")
    else:
        print("2. Search at a moderate speed                8. Locked")
    if build:
        print("3. Search at full speed                      9. Build Termination Code")
    else:
        print("3. Search at full speed                      9. Locked")
    if destroy:
        print("4. Search for supplies                       10. Destroy the AI")
    else:
        print("4. Search for supplies                       10. Locked")
    if instructions:
        print("5. Status check                              11. Instructions for unlocked commands")
    else:
        print("5. Status check                              11. Locked")
    if status:
        print("6. quit                                      12. Unlocked command, status check")
    else:
        print("6. quit                                      12. Locked")
    print()
    print()
    choice = int(input("Choose a command ==> "))
    print()
    print()
    if choice == 1 and supplies > 0:
        rand = random.randrange(0, 11)
        if rand == 10 and not magnet:
            print("You built a Magnet with some of your supplies!")
            print("You now have a additional command you can use.")
            magnet = True
            status = True
            instructions = True
        rand = random.randrange(0, 11)
        if rand == 10 and not attack:
            print("You built a gun with some of your supplies!")
            print("You now have a additional command you can use.")
            attack = True
            status = True
            instructions = True
        supplies -= 1
        print("Your command before needing to use supplies has been reset to 7")
        life = 7

    elif choice == 2:
        rand = random.randrange(0, 7)
        if rand == 6:
            print("You found a bag of supplies!")
        supplies += 1
        rand = random.randrange(0, 16)
        if rand == 15:
            print("You found a termination code part!")
            codeParts += 1
        life -= 1
        rand = random.randrange(6, 15)
        robotDistance += rand
        print("The Robots are ", robotDistance, " miles behind you")
        rand = random.randrange(6, 31)
        gas -= rand
        print("You have ", gas, "% gas left in your motorbike")
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")

    elif choice == 3:
        rand = random.randrange(0, 5)
        if rand == 4:
            print("You found a bag of supplies!")
        supplies += 1
        rand = random.randrange(0, 13)
        if rand == 12:
            print("You found a termination code part!")
            codeParts += 1
        rand = random.randrange(1, 3)
        life -= rand
        rand = random.randrange(6, 20)
        robotDistance += rand
        print("The Robots are ", robotDistance, " miles behind you")
        rand = random.randrange(15, 41)
        gas -= rand
        print("You have ", gas, "% gas left in your motorbike")
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")

    elif choice == 4:
        rand = random.randrange(0, 2)
        if rand == 1:
            print("You found a bag of supplies!")
            supplies += 1
        rand = random.randrange(0, 11)
        if rand == 10:
            print("You found a termination code part")
            codeParts += 1
        rand = random.randrange(6, 15)
        robotDistance -= rand
        print("The Robots are ", robotDistance, " miles behind you")
        life -= 1
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")

    elif choice == 5:
        print("S T A T U S   C H E C K")
        print("Small bags of supplies: ", supplies)
        print("Termination code parts: ", codeParts)
        print("Commands before needing to use supplies: ", life)
        print("Commands before Robots take over the world: ", robotComm)
        print("Your motorcycle is ", gas, "% full of Gas")
        print("The robots are ", robotDistance, "miles behind you")
        check = True

    elif choice == 6:
        done = True
        break

    elif choice == 7 and attack:
        rand = random.randrange(4, 9)
        print("You found", rand, "bags of supplies!")
        supplies += rand
        rand = random.randrange(0, 7)
        if rand == 6:
            print("You found a termination code part")
            codeParts += 1
        rand = random.randrange(6, 15)
        robotDistance -= rand
        print("The Robots are ", robotDistance, " miles behind you")
        life -= 1
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")
        rand = random.randrange(0, 5)
        if rand == 4:
            print()
            print("Some of the robots you attacked have captured you.")
            print("Luckily the robots don't want to have to cut you up and make you into a cyborg.")
            rand = random.randrange(3, 13)
            print("So the robots offered you a deal of ", rand, "little bags of supplies for your life")
            print()
            print()
            if rand > supplies:
                rand = random.randrange(0, 2)
                if rand == 1 and codeParts > 0:
                    print("You did not have enough supply parts. So instead you gave them your termination")
                    print("code parts and they let you go.")
                    codeParts = 0
                else:
                    print("You did not have enough supplies so you failed to save the world")
                    print("and the robots turned you into a angry cyborg.")
                    break
            else:
                print("S U B   C O M M A N D S")
                print("1. Give the payment for your life")
                print("2. Try to escape")
                print()
                choice = int(input("Choose a command ==> "))
                print()
                if choice == 1:
                    supplies -= rand
                    print("You payed them the ", rand, " supplies and they let you go.")
                elif choice == 2:
                    rand = random.randrange(0, 4)
                    if rand == 3:
                        print("You tried to escape but the robots shot you in the back while trying to run")
                        print("for the trees. And the robots turned you into a angry cyborg.")
                        break
                    else:
                        print("You successfully made it to the trees before the robots could stop you.")
                else:
                    print("You decided just to stand there so the robots got annoyed and killed you.")
                    break

    elif choice == 8 and magnet:
        rand = random.randrange(0, 5)
        supplies += rand
        print("You found ", rand, " bag of supplies!")
        rand = random.randrange(0, 10)
        if rand == 6:
            print("You found a termination code part")
            codeParts += 1
        rand = random.randrange(6, 15)
        robotDistance -= rand
        print("The Robots are ", robotDistance, " miles behind you")
        life -= 1
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")

    elif choice == 9 and build and supplies > 29:
        supplies -= 30
        destroy = True
        codeParts -= 6
        print("The termination code has now been built next turn you can destroy the AI")
        robotComm -= 1
        print("You have ", robotComm, "commands before robots take over the World!")
        life -= 1
        rand = random.randrange(6, 15)
        robotDistance -= rand
        print("The Robots are ", robotDistance, " miles behind you")

    elif choice == 10 and destroy:
        win = True

    elif choice == 11 and instructions:
        if attack:
            print("Attacking the robots is a more riskier way to get supplies and termination code parts but")
            print("you can get alot more of those rewards.")

        else:
            print("Locked")
        print()
        if magnet:
            print("Using the magnet can earn you more supplies than searching for supplies but less")
            print("supplies then attacking the robots but the magnet is safer.")
        else:
            print("Locked")
        print()
        print("Building the termination code will unlock the command destroy the AI which will")
        print("allow you to win the game on the next turn ")

    elif choice == 12 and status:
        print("S T A T U S   C H E C K")
        if attack:
            print("You have unlocked the command attack the robots.")
        else:
            print("Locked")
        if magnet:
            print("You have unlocked the command use magnet.")
        else:
            print("Locked")
        if destroy:
            print("You have a termination code.")
        print("Small bags of supplies: ", supplies)
        print("Termination code parts: ", codeParts)
        print("Commands before needing to use supplies: ", life)
        print("Commands before Robots take over the world: ", robotComm)
        print("Your motorcycle is ", gas, "% full of Gas")
        print("The robots are ", robotDistance, "miles behind you")
        check = True

    else:
        print("That is not a command choice!")

    if life < 1:
        print("You forgot to drink water and eat food")
        print("if your gonna save the world you have to at least try a little bit harder than that.")
        done = True
        break
    elif gas < 1:
        print("You ran out of gas in your motorcycle and the robots caught up to you.")
        print("Remember to check your gas next time.")
        done = True
        break
    elif robotComm < 1:
        print("You took too long to save the world the robots have now infested the world and are killing everyone")
        print("in it including you.")
        done = True
        break
    elif robotDistance < 1:
        print("The robots caught up to you and made you into a angry cyborg.")
        print("Remember to stay away from the robots next time. ")
        done = True
        break
    if win:
        print("You destroyed the AI and won the game!")
        done = True
        break
    rand = random.randrange(0, 10)
    if rand == 9 and not check:
        print()
        print()
        print("You found a gas station you now have 100% gas in your motorcycle")
        gas = 100
    check = False
