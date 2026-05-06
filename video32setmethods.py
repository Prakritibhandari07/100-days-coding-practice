s1={1,2,3,4}
s2={5,6,4}
print(s1.union(s2))

print(s1,s2)
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s1.intersection_update(s2)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.add(6))
print(s1.discard(5))
s1.pop()

