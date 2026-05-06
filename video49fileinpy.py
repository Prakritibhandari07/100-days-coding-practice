# f=open('myfile.txt','r')
# text=f.read()
# print(text)
# f.cloe()

# f=open('myfile.txt','a')
# f.write('hello world!')
# f.close()

with open('myfile.txt','a') as f:
    f.write("Hey I'm inside with")