dic={
    "Harry":"Human being",
    "Spoon":"Object"
}
print(dic["Harry"])
print(dic.get("Harry"))
for key in dic.keys():
    print(f"The value corresponding to the key{key} is {dic[key]}")