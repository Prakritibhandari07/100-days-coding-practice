class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of Employee:{self.id} is {self.name}") 


class Programmer(Employee):
    def showLanguage(self):
        print("The default Language is Python")


e1=Employee("Prakriti","101")
e1.showDetails()   
e2=Programmer("Pranil","103")
e2.showLanguage() 
e2.showDetails()      
