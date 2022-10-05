  #Sign your name:Aidan Zimmerman
import random
'''
    1. Make the following program work.
'''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
     x = int(input("Enter a number: "))
     total = x + total
print("The total is:", total)


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
     print (i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10
while i > -1:
     print(i)
     i=i-1
print ("Blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

print(random.randint(1,10))




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
q=0
w=0
e=0
x=0
for i in range (0,7):
     num=int(input("Give me a number "))
     if num == 0:
          q+=1
     elif num <= 0:
          w+=1
     else:
          e+=1
     x+=num
print("The sum of these numbers is",x)
print("There were",q,"zeros")
print("There were",w,"negative numbers")
print("There were",e,"positive numbers")
