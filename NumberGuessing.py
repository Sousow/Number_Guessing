import random
import math
lower=int(input("Enter Lower bound:-"))
upper=int(input("Enter Upper bound:-"))
x=random.randint(lower,upper)
print("\n\t You've only ", round(math.log(upper-lower+1,2)),"chances to guess the integer!\n")
count=0
while count<math.log(upper-lower+1,2):
    count+=1
    guess=int(input("Guess a number:-"))
    if x==guess:
        print("\n Congrats,count:",count)
        break
    elif x>guess:
        print("Guess is small!")
    elif x<guess:
        print("Guess is high!")
if count >=math.log(upper-lower+1,2):
    print("\n The number is %d" %x)
    print("\t Better luck next time!")