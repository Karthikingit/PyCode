# conditional statements


"""# logical operators
a==b
a!=b
a<b
a<=b #results are true or false
"""

a = 2380
b = 2380
if a > b:
    print("a is great")
elif b > a: print("b is great")
else:
    print("equal")
# alternate method
print("a is greater ") if a > b else print("b is great")
#and operator
a = 344
b = 399
c = 432
if b>a and c>a:
    print("any")
#or

a = 344
b = 399
c = 432
if b > a or c > a:
    print("or operator")

#functions

def trialfunction(x,y):
    print(x+y)
trialfunction(25,87) #25 and 87 are argument x,y is parameter
 
#for and while loop
#for loop
numbers = [1,2,34,56,78,91,100,22123]
for x in numbers:
    print(x)
e = "fruits and nuts"
for a in e:
    print(a)
numbers = [1, 2, 34, 56, 78, 91, 100, 22123]
for x in numbers:
    print(x)
    #for breaking break
    if x==100:
        break
    #continue, resume after def value
numbers = [1, 2, 34, 56, 78, 91, 100, 22123]
for x in numbers:
    if x == 34:
        continue
    print(x)

#start from def or start from 0 if not defined and end bfore definrd value
for x in range(35,100):
    print(x)


#while loop
r = 1
while r<23:
    print(r)
    r += 2

 #break and continue in while
r = 1
while r < 23:
    print(r)
    if r == 17:
        break
    r += 2

r = 1
while r < 23:
    r += 2
    if r == 17:
        continue
    print(r)


#FUNCTIONS AS ARGUMENTS

mul = ("car","bike","ship")

def funname(x):
    print(x*2)

funname(mul)
     #map function
def mapinfun(crazy,mul):
    for items in mul:
        crazy(items)

mapinfun(funname,mul)

#functions exercise
def any_highest(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)

print(any_highest( [2,4,6,8,10,24,35,23] ))