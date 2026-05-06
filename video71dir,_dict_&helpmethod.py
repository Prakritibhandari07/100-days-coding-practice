x=(1,2,3)
print(dir(x))
print(x.__add__)
#The dir() function returns a list of all the attributes 
#and methods available for the object.


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("Prakriti",18)
print(p.__dict__)        

#dict=helps to change any form into dictionary
print(help(str))
print(help(Person))
#The help function is used to used to get help documentation
#for an object,including a description of it's attributes
#and methods.

