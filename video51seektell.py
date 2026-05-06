with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    #Move to the 10th byte in the file
    data=f.read(5)
    #read the next file bytes
    print(data)


with open('myfile.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('myfile.txt','r') as f:
    print(f.read())