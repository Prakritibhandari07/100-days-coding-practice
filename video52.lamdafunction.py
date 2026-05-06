# def double(x):
#     return x*2

double=lambda x:x*2

print(double(5))


square=lambda x:x^2
print(square(2))

cube=lambda x:x*x*x
print(cube(5))

avg=lambda x,y,z: (x+y+z)/2
print(avg(3,5,8))

print(cube(lambda x:x*x*x,2))