class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls,string):    
        return cls(string.split("_")[0],string.split("_")[1])

e1=Employee("Harry","12000")
print(e1.name)
print(e1.salary)     

string="John_12000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)  
