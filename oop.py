#OOPS
class GameObject:  #use camelcase for naming
    def __init__(self, name, age):   #if we dont have any variables or attributes assign to the class __init__ is not needed 
        self._name = name  #for indicating it is private variables
        self._age = age
    
    def Playerrun(self):
        print('run')
        return('something')

    def shout(self):
        return(f'returning from f string {self._name}, {self._age}')

player1 = GameObject('Andy',23)
player2 = GameObject.Playerrun('run')
print(player1.shout())
print(player2)

#Encapsulation - combining or bindding datas

#Abstratction - accessing methods we defined juz like accessing default predef methods (givin access only to what is needed and hiding else)
     #e.x accessing only what methods we need 

#Inheritance - allows new obj to take on the properties of existing objects
class InhertanceGaming:
    def sign_in(self):
        print('logged_in')

class Wizard(InhertanceGaming):
    def __init__(self, name , power):
        self._name = name
        self._power = power
    def attack(self):
        print(f'attacking with power of archer {self._power}')

class Archer(InhertanceGaming):
    def __init__(self,name , rem_arrows):
        self.name = name
        self.rem_arrows = rem_arrows
    def attack(self):
        print(f'attacking with the power of archer, rem arch-{self.rem_arrows}')

playerWi = Wizard('Wizzy',35)
playerArc = Archer('Kelly',45)

playerWi.attack()
playerArc.attack()

#Polymorphism - diff object classes share method names, but each one functionality differs baseed on arretibutes
def char():
    playerArc.attack()
    playerWi.attack()
    #using for
for char in [playerWi,playerArc]:
    char.attack()

#__dundermethods__ - this allows us to use specific functions to our objects created to our class, we won't write own dunder methods
from subprocess import call

class Toy():
    def __init__(self, colour,age):
        self.colour = colour
        self.age = age
        self.my_dict = {'Name':
        'Karthik',
        'Age': '23'}
    
    def __len__(self): #juz defining what to do 
        return 5
    
    def __str__(self):
        return f'{self.colour}'
    
    def __call__(self):
        return('yess!')

    def __getitem__(self , i):
        return self.my_dict[i]
    
action_figure = Toy('Black',22)
print(len(action_figure))
print(action_figure.__str__())
print(str(action_figure))
print(action_figure())
print(action_figure['Name'])
