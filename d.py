d={
    "Name":"Priyanshu",
    "Marks":15.2,
    "Age":19
}
# print(d["Marks"])
# print(len(d))
# d['Marks']=50
# d['trade']="CSe"
d.update({'trade':"cse"})
# print(d.items())
# d.pop("Marks")
# d.clear()
d.values()
# print(d.values())
print(type(d))

for i in d:
    print(f"Keys {i} is {d[i]}")