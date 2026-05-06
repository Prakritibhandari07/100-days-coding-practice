countries=("Nepal","India","China")
countries2=("Bhutan","Japan","Korea")
SouthEastAsia=countries+countries2
print(SouthEastAsia)
tuple=(1,2,3,4,2,3,4)
res=tuple.count(4)
print("count of 3 in tuple is:",res)
res2=tuple.index(3)
print("index of 3 in tuple is:",res2)
res3=tuple.index(4,4,6)

#tuples are immutable i.e they cannot be changed.
#for eg. tup[0]=23,it cannot happen.