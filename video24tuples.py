tuple=(1,2,3,4,5,"Prakriti")
print(type(tuple),tuple)
print(len(tuple))
print(tuple[0])
print(tuple[-1])
if"Prakriti" in tuple:
    print("Yes Prakriti is present in tuple.")
tuple2=tuple[1:5]
print(tuple2)
print(tuple[0:])
print(tuple[:])
print(tuple[:4])    