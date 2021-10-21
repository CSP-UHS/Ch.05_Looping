  #Sign your name:____Jaxson____________


# 1. Make the following program work.

total = 0
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total+= x

print("The total is:", total)




  #2. Write a Python program that will use a FOR loop to print the even
    # numbers from 2 to 100, inclusive.

for i in range(2,101,2):
    print(i)
print("Done")







  #3. Write a program that will use a WHILE loop to count from
     #10 down to, and including, 0. Then print the words Blast off! Remember, use
    # a WHILE loop, don't use a FOR loop.

import time
count = 10
while count>-1:
    time.sleep(0.5)
    print(count)
    count-=1
print("Blast off!")





  #4. Write a program that prints a random integer from 1 to 10 (inclusive).


import random

for i in range(1):
    num = random.randint(1,10)
    print(num)
print("Done")
`




   
  #5. Write a Python program that will:
     
    # * Ask the user for seven numbers
    # * Print the total sum of the numbers
     #* Print the count of the positive entries, the count of entries equal to zero,
     #and the count of negative entries. Use an if, elif, else chain, not just three
     #if statements.
negative = 0
positive = 0
zeroes = 0
total = 0
for i in range(7):
    user_input = int(input("Please choose a number: "))
    total += user_input
    if user_input > 0:
        positive+=1
    elif user_input <0:
        negative+=1
    else:
        zeroes+=1
    total+= user_input
print("The total sum is:",total)
print("Amount of positives:", positive)
print("Amount of negatives:", negative)
print("Amount of zeroes:", zeroes)



