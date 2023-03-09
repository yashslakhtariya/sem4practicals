# enumerate

lst = [64, 16, 32, "Haribol", True]

# for index, item in enumerate(lst):
#      print(index, item)
     
for a, b in enumerate(lst):
     print(a, b)

print("\n\n")

# list_comprehension

lst2 = [16, 32, 64, 192]
tmp = []

for item in lst2:
     tmp.append(item)
     
print(tmp)
