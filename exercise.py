#fibonacci series
def fibon(num):
    a = 0
    b = 1
    for i in range(num):       
        yield a
        temp = a
        a = b
        b = temp+b
        
for x in fibon(21):
    print(x)

from multiprocessing.managers import ValueProxy
from operator import truediv
import oop
print(oop) #to inmport module in package package.module

#to print series of numbers  
print(tuple(input("Enter a series of numbers separated by a comma :").split(',')))


from random import randint
answer = randint(1, 10)
print(answer)

while True:
    try:
        print(answer)
        guess = int(input("Guess the number: "))
        if guess < 0 and guess > 11:
            if guess == answer:
                print("Good")
                break
        else:
            print("Enter number 1~10")
    except ValueError:
        print("Enter number")
        continue

