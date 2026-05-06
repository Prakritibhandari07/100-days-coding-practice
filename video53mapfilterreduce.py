#map
# def cube(x):
#     return x*x*x

# print(cube(2))

l=[1,2,3,4,5]
# newl=list(map(cube,l))
#newl=list(map(lambda=x:x*x*x,l))
# print(newl)

# #filter
# def filter_function(a):
#     return a>2
# newnewl=list(filter(filter_function,l))
# print(newnewl)

#list of numbers
numbers=[1 ,2 ,3 ,4, 5]

# calculate the sum of numbers
# using the reduce function
def mysum(x,y):
    return x+y

sum= reduce(mysum,numbers)
#print the sum
print(sum)

