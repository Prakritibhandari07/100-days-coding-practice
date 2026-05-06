list=[4,5,6,"Harry",True]
Marks=[4,5,6,7,9,"Harry","Prakriti",True]
print(list)
print(type(list))
print(list[0])
print(list[4])
print(list[3])
print(list[-2])

if "Harry" in list:
    print("yes")
else:
    print("No")    

if "Ha" in "Harry":
    print("Yes")
else:
    print("No")       

print(Marks[7])
print(Marks[-6])    
print(Marks)
print(Marks[1:5])
print(Marks[1:5:7])


lst=[i*i for i in range(4)]
print(lst)

listt=[i*i for i in range(10) if i%2==0]
print(listt)
