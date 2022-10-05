'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
q=0
w=0
for i in range(0,51):
    x=random.randint(0,1)
    if x==0:
        print("Heads")
        q+=1
    else:
        print("Tails")
        w+=1
print("There were",q,"heads")
print("There were",w,"tails")







