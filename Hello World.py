# multiline comment

"""
usdbcib
dcjbidi

"""
# data types
x = 1
y = 1.4
z = 1j

print(type(x))
print(type(y))
print(type(z))

#convert int to float
a=float(x)
#float into int
b = int(y)
#con float into complex
c = complex(x)
print(a)
print(b)
print(c)
#follows BODMAS 1st () 2nd **
#adding var 
"""must start with lowercase
snake case
can be letter,no.,undrscores
case sensitive
don't overwrite keywords"""
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)
x = (a/b*c)
print(x)

e = (a%b)#modulus give remainder , important
t = (a**b)# exponent powerofpower
i = (a//b)#floor division returns nearest rondoff value

print(e,t,i)

#common errors
""" 1. syntax errors
2.index errors in list 
3. import error, calling undef module
4. dict error - key error
5. import error from module math search for cube which is not exist
6.iteration error 
7.type error ,adding str and int
8.value error, int("jdf")
9.name error,calling  undefined var
10.zerodiverror, division by zero
11. keyboard error, without giving input at output enter name
12. intendation error, allignment error """

x = 45
print(x)

#changing type of inp
x = str(5)
y = int(5)
z = float(5)

print(type(x),type(y),type(z))

#var are case sensitive, _car_door a23jns
#multi assign value
x,y,c = "jhsdb", 8, 5.3

#multiline strings
x = """Orange
are in orange colour"""
y = '''Apple are
 i
 n red 
 colour'''
print(x,y)

#string like a array
x = "Hello ,from the world"
print(len(x))
for a in x:
    print(a)

#in oprator -returns result in  boolean
x = "Hello ,from the world"
print("from" in x)
print(("like" in x))

#slicing
print(x[2:6]) #stop before 6th char..
print(x[2:])
#for reverse slincing
print(x[-5:-2])
print(x[-8:])
#lower and upper case
print(x.upper())
#strip
x = "Hello ,from the  world@gmial.com    "
#strip remove unnecess spaces
print(x.strip())
#replace
print(x.replace("H", "r"))
#split into array after the mentioned char
print(x.split("@"))

#concordination, add stuff between two var val
a = "Hello"
b = "world"

print(a+ " and the " +b)

#Agmented assignment operator
some_value = 5
#instaed of giving like some_value = some_value + 3
some_value += 3
print(some_value)

#Escape sequence 
#instead of typing 'It's Sunny' - it will be type error
a = "It's sunny" #use double quotes or...
b = "It's \"kinda\" sunny" #whaterver comes after \ it will recog as a string
print(b)
#another ex
weather = "It's\\kinda sunny" #recog the second \ as a string so it prints that
print(weather)
weather2 = "\t It's kinda \n sunny"
print(weather2)   #\t for adding tab and \n for print in new line

#formatted strings
name = "johnny"
age = 25
print("hi " + name + " you're " + str(age)  + " old")

#instead of this we declare this is a formatted str by
print(f"hi {name}, You're {age} years old")
#another .format
print("hi {}, You're {} years old" .format(name, age))

#string indexes also called
selfish = "0123456789"
#          0123456789
print(selfish[0:9]) #start:stop
print(selfish[0:9:2]) #start:stop:stepover


