import pickle

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.address})"

listPeople=[]
while(True):
    name=input('get name:')
    age=input('get age:')
    address=input('get address:')
    newPerson=Person(name, age, address)
    f=open(file.dat,'ab')
    listPeople.append(newPerson)
    goAhead=input("do you want countinu?[Y,N] ")
    if goAhead=='N':
        break

    
