lst = ["ICT", "Guni", "Ahmedabad"]

tmp = lst.pop()
print(tmp)
print(lst)

lst = ["ICT", "Guni", "Ahmedabad", "ICT"]
lst.remove("ICT")

lst.count("ICT")

lst.reverse()
y = lst.sort()
print(y) # y = none

lst.sort(reverse=True)

lst = ["Ict", "Guni", "Ahmedabad", "ICT"] # reverse gives Ict first and then ICT because ascii(c)>ascii(C)

print(lst)

exit()