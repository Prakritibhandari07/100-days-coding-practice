def average(a,b):
    print("The average is",(a+b)/2)
average(5,4)    

def average(a=8,b=6):
    print("The average is",(a+b)/2)
average(a=4)


def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))

average(5,6)           


def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)    
c=average(7,8,9,6)
print(c) 