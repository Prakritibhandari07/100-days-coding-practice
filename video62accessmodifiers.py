# Access specifiers in python programming 
# are used to  limit the access of class variables
# and class methods outside of class while implementing the concepts 
# of inheritance.
#  Types of access modifiers:
# 1.Public access modifiers
# 2.Private "       "
# 3.Protected "       "


#Private:
class Employee:
    def __init__(self):
        self.__name="Prakriti"


a=Employee()
a.emp1=5
#print(a.name) cannot be accessed directly.
print(a._Employee__name) #can be accessed directly.
print(a.__dir__())


#Protected:
class Student:
    def __init__(self):
        self._name="Pranil"

    def _funName(self):       #protected
        return "Puzzu"
    
class Subject(Student):         #inheritance
    pass

obj=Student()
obj1=Subject()

print(obj._name)#calling by object of student class
print(obj._funName())
print(dir(obj))
print(obj1._name)#calling by object of subject class
print(obj1._funName())


