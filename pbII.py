#short circuiting 
import enum
from shutil import unregister_unpack_format
from typing import ItemsView
from winreg import EnumValue
from xml.dom import UserDataHandler


andy = False
Mandy = True

if andy or Mandy:
    print('Anything')

#loops
anynamen = {'name': 'karthik',
'age': 24,
'subject': ['math,science']}

a = (1,23,34,45,56,23)
b = ('a','b','c','d','e','f','g')
for h in a:
    for w in b:
        print(h,w)
for y in anynamen.items(): #for getinf key val pairs in dict
    print(y)
for x in anynamen.values(): #val
    print(x)
for item in anynamen.keys(): #keys
    print(item)

#counter exer
asdj = [1,2,3,4,5,6,7,8,9,10]
we = 0

for r in asdj:
    we = we+r
print(r)

#range - prod obj from start to stop

for dfs in range(0,100):
    print(dfs)

#enumerate - indexing the item that we iterate

for i,any in enumerate((1,212,23,24,34,23,12,23)):
    print(i,any)

for i,sdjcn in enumerate(list(range(16))):
    if sdjcn == 12:
        print(f'index od 12 is: {i}')

#while loop
a = 23
while a < 50:
    print(a)
    a += 1
else:
    print("done")

#for is for simple loops , while is for we're not sure abt how many times loops should occur
#continue ,beeak, pass-does'nt do anything

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for img in row:
        if (img == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


