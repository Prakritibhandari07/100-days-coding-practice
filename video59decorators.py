 #Decorators are a powerful and flexible feature 
#in Python tha can be used to add functinality to
#functions and methods without modifying their source code.

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
        return mfx


@greet
def hello():
    print("Hello world")

def add(a,b):
    print(a + b)
add(a=4,b=5)  

# greet(hello)()
hello()
greet(add)(1,2)