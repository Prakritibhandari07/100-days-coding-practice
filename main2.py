# a=input("Enter your name: ")
# print("My name is",a)
# x=input("Enter first number: ")
# y=input("Enter second number: ")
# print(x+y)
# print(int(x)+int(y))
# print(int(x)-int(y))
# print(int(x)/int(y))
# print(int(x)*int(y))
# print(int(x)//int(y))
# print(int(x)**int(y))
# print(int(x)%int(y))
# print(5**4)

#r-only view the file
#w-write something inside the file.
#a-modify the file,append the file,make changes
#r+-both reading and writing
# file=open("sample.txt","r")
# print(file.readlines())
# file.close()

# #writing files
# file=open("myfile.txt",'w')
# print(file.writelines())
# file.close()

coun_file=open('myfile.txt')
coun_file.write('\nThis is new line.')