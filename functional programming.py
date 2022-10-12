#instead of seperating data and functions instead of methods and attributes
# pure function doesnt affect he outside world
#map,filter,zip,reduce are diff functions
# map - allows to simplifies the code
def funname(item):
    return item * 2

print(list(map(funname, [2,2,1])))

#filter - it fileter things
listname = [2,3,4,46,76]

def findingnemo(item):
    return item % 2 == 0

def findingdory(item):
    return item % 2 != 0

print(list(filter(findingdory, listname)))
print(listname) #it doesnt impact on var thatshow pure function should be

#zip
var_1 = [2,34,45,56,12]
var_2 = (92,334,54,56)

print(list(zip(var_1, var_2)))

#reduce - it is not a part of built in py fun

#lambda exppression - onetime anonymous functios
listmyine = [23,34,45,56,67]

print(list(map(lambda item: item*4 , listmyine)))
print(list(filter(lambda item: item % 2 != 0 , listmyine)))
print(listmyine)

#Lambda exercise
listinlambda = [23,243,351,2]
listinlamb2 = [(9,9),(2,1),(3,0)]
print(list(map(lambda item: item **2 ,listinlambda )))
listinlamb2.sort(key = lambda x: x[0])
print(listinlamb2)

#comprehensions
#list comprehension
lc1 = [any for any in "helloworld"]
print(lc1)
lc2 = [num**2 for num in range(0,100)]
print(lc2)
l3 = [aun**3 for aun in range(0,10) if aun % 2 == 0]
print(l3)
#set comprehension - set doesn't allows duplicate 
lcd = {any for any in "helloworld"}
print(lc1)
lcf = {num**2 for num in range(0,100)}
print(lc2)
lw = {aun**3 for aun in range(0,10) if aun % 2 == 0}
print(l3)
#for printing duplicates in list 
ai = [1,1,23,344,2,12,23]
pi = set(list([x for x in ai if ai.count(x) > 1]))
print(pi)