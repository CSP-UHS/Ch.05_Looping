#Looping
import random
# for i in range(100,-1,-2):
#     print(i)
# for i in [1,2,3,4,5,6,7]:
#     print(i)
#
#
# done = False
# perseverance = 0
# while not done:
#     quit = input("Do you want to quit? (type y)")
#     if quit.lower() == "y":
#         done = True
#     else:
#         perseverance+=1
# print("Goodbye! Your perseverance level is ", perseverance)

# for i in range(10):
#     num = random.random()*5+10
#     print(num)

round1=1
y=1
attempts = 0
done = False
print("Welcome to higher or lower")
print("Guess numbers between 1 and 100")
while done==False:
    x = random.randint(0, 100)
    while y==1:
        attempts+=1
        guess = int(input("guess: "))
        print()
        if guess == x:
            print("Congrats, it took you",attempts, "guesses")
            y=2
        elif guess>x:
            print("Lower")
        elif guess<x:
            print("Higher")
    play=input("Would you like to play again? (y or n):")
    if play == "y":
        y=1
        round1+=1
        attempts=0
        print("Round",round1)
    else:
        done=True