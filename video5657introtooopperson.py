#INTRODUCTION TO OOP IN PYTHON
#VIDEO-56

#  oop uses concept of object and classes to represent real
#  real-world entities.
#A class is a blueprint or template for creating object.


#PYTHON CLASS AND OBJECTS
#VIDEO-57

#Self-parameter is a reference to the current instance of the class,and is used
#to access variables that belongs to a class.

class Person:
    name="Prakriti"
    occupation="student"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    # print(f"{name} is a {occupation}")


a =Person()
b=Person()
c=Person()
a.name= "Pranil"
a.occupation="Software Engineer"
b.name="Lila"
b.occupation="Teacher"
a.info()
b.info()
c.info()