#list called as array in other language it is mutable
#can store any value
import os

l1 = ["any","sunny",1,1.3,True]
#prop of list

""" it is order items i.e changeable, we can add 
"""
print(len(l1))
print(l1[4])
print(l1[-4])
#mofdifying in list
l1[2] = "scooters"
print(l1)
#insert fun in list
l1.insert(3, "jeep")
print(l1)
#append fun in list add the input at last of the list
l1.append(23)
print(l1)
#tuple is unchangeable,ordered(while giving output) and allow duplicated other than this smae as list uses () we can say tuple is immutable list
#if u dont need to change list we use tuple
tuplename = (1,2,3,3,443,3,55,2)
'''tuplename[1] = 4
print(tuplename) - it throws an error coz it is immutable'''
print(443 in tuplename)
x,y,z,r, *other = (1,3,2,1,23,244,1234,234)
print(x,y,z,r)
print(other)

#dictionary is unordered(while giving output),not allow duplicates,changeble uses{}
#in list we give 1,2,3 as a index in dict we give keys are index
#can store key-value as an array...
dictanyname={
      "name":"Raj","District":"TVM"
,"Bike":["Pulsar","Rs","ns"],"name":"Ram"}
print(dictanyname)
print(len((dictanyname)))
x = dictanyname["name"]

print(x)
dictanyname
#dict keys should be always immutable,unique
#dict methods - to access keys use .get method
dictname = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth'
}
print(dictname.get('Status'))
#if key is not exist to set default val for the same
dictnamine = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth'
}
print(dictnamine.get('age', 34))
#check what it returns if key exists
dictnamine2 = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth',
    'age': 233
}
print(dictnamine2.get('age', 34))
#crete user with key val pairs!
userdictname = dict(name='Kinder')
print(userdictname)
#how to look for an item in a dict we use "in"
print("class" in dictnamine2)
#for check in keys use xxxxx.keys for values use xxxxx.values
print('age' in dictnamine2.keys())
print('tenth' in dictnamine2.values())
#for items key+val of 1 whole item
print(dictnamine2.items())
#list comprehension, larger piece of code is combined into small once
#used in ML and data oriented application---writing for loop items in one line by making it flat

fruits=["apple","banana","orange","kiwi","pine"]
newfruits = []
for x in fruits:
      if "a" in x:
            newfruits.append(x)
print(newfruits)

     #list comprehension for above code

automobiles = ["pulsar","m4","gt","roma","continental"]
newautomotives = [x for x in automobiles if "a" in x ] #can use range, if else
print(newautomotives)
new2auto = [x  if x!="roma" else "911" for  x in automobiles]
print(new2auto)
new3auto = [x.upper() for x in automobiles ]
print(new3auto)


#file handling, r for reading
f = open("dummy.txt" , "r")
print(f.read())
#read util 1st line
k = open("dummy.txt" , "r")
print(k.readline())
#for 2nd line
print(k.readline())
#read line for read gn line
m = open("dummy.txt" , "r")
print(m.readline(8))
#keep close the file after open
f.close()
k.close()
m.close()
#file append, adding at laste is append
f = open("dummy.txt","a")
f.write("ijbdijjajsfvno A new line")
f.close
#print in read mode
m = open("dummy.txt","r")
print(m.read())
m.close()

#write mode,overwirte the stuff
m = open("dummy.txt","w")
m.write("A line 2 new added")
m = open("dummy.txt","r")
print(m.read())
m.close()
'''
os.remove("newtextfile.txt")
import os
if os.path.exists("newtextfile.txt"):
      os.remove("newtextfile.txt")
else:
      print("File not found")

#create mode - x , create a new file
f = open("newtextfile.txt","x") #write mode also create file
f.close()
#to delete
'''

#sets - unordered coll of unique object
my_sets = {1,2,23,23,43,43}
print(my_sets) # returns only unique 
listinname = [2,2,2,2,4,3,45,4,5,5,56]
print(set(listinname)) #to remove duplic.. in a list
#methods in sets
setone = {2,23,34,23,43}
secset = {43,45,234,45,65,34}
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()
