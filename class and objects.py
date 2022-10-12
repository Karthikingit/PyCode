"""grp of fun and var is called
 class we can also called like template """

class Human:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def methodname(self):
        print("Hi my name is " + self.name + ", My age is " , self.age )
        
h1 = Human("Sherlock Holmes", 23)
h2 = Human("Sheela", 23)
del h1
h2.methodname()

#lambda, filter and maps
"""
lambda is writing function in oneline 
filter and maps apply on some list"""

t = lambda a: a+203
print(t(5))
#multi val and parameter
y = lambda r,g,h: r+g-h
print(y(5,7,9))
#lambda in fun
def f1(n):
    return lambda q,w,e: q+w-e

doub = f1(2)
#can use many object
tri = f1 (34)

print(doub(11,23,44))
print(tri(23,53,23))

#filter, filter from list
def prime(x):
    for n in range(2,x):
        if x%n == 0:
            return True
        else:
            return False
filtername =filter(prime,range(55))
print("The filtered prime no. are ",  list(filtername))

#map and filter could apply on some seq that seq could be list , tuple, dict

def anyname(x):
    return x*23
nums = [3,5,34,2,3,23,434,34]
anysecname = map(anyname,nums)
print(list(anysecname))

#py pip, py package installer - lib ref as package are code written by others

import camelcase

x = camelcase.CamelCase()

a = "hi there is an new message arrived"

print(x.hump(a))

"""to read excel file"""

#for opening xlsx file
""" import xlrd
locanyname = ("D:\\Downloads\\IamKarthik_codecommit_credentials.xlsx")

wb = xlrd.open_workbook(locanyname)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(1,1)) """

#iterator it is substitute for for loop
#it is easy straight frwd not like for loop

tuple1 = ("any","car","bike")
nameany = (iter(tuple1))

print(next(nameany))
print(next(nameany))
print(next(nameany))
#another ex. for iterator
tuple12 = ("anycanprint")
nameany2 = (iter(tuple12))

print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))
print(next(nameany2))

#pickling- to store ad reload your model or data like for encryption
import pickle

mydict = {"1":"a","2":"b"}
pickle_file = open("picklefile.txt","wb")
pickle.dump(mydict, pickle_file)

pickle_file = open("picklefile.txt","rb")
new_dict = pickle.load(pickle_file)

print(new_dict)

#python json - data sharing

"""import json

person ='{"Name": "Mohan", "Class": "HSC", "Sub": ["Maths","Eng",Tam"]}'
peron_dict = json.loads(person)

print(peron_dict)
print(peron_dict["Sub"])"""