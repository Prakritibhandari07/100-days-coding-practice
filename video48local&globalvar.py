x=5

def hello():
    global x
    x=6
    y=7
    print(f"The local x is {x}")
    print(f"The local y is {y}")

print(f"The global x is {x}")
hello()
z=8
print(z)