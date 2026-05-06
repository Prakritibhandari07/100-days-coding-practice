class Employee:
    companyName="Google"
    noofEmployee=3
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noofEmployee} in {self.companyName} is  is {self.raise_amount}")   

emp1=Employee("Prakriti")     
emp1.raise_amount=0.3
emp1.showDetails()  
emp2=Employee("Pranil")
emp2.companyName="Apple"
emp2.showDetails()