list_org = ["banana", "cherry",  "apple"]

list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [x*x for x in mylist]

print(mylist)
print(b)