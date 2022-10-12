from enum import Flag
from sys import flags
from turtle import title


def udemytry(f_name, l_name):
    return (f_name.title(),l_name.title())

print(udemytry('knis sdnci','sdkmfi ksndinc'))


number = int(input("Enter the number: "))
#
if number > 1 :
    for i in range(2,number):
        if (number % i == 0 ):
