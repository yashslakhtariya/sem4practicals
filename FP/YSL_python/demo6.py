lst = [0,1,(0,1)]

print(lst)

lst[2][1] = 2       # error : tuple cannot be edited

tpl = (0,1,[0,1])

tpl[2][1] = 2       # done : list inside tuple can be edited

print(tpl)

lst2 = [0,1,[0,1]]

lst2[2][1] = 2      # done ofcourse : list inside list can be edited

print(lst2)

tpl2 = (0,1,(0,1))

tpl2[2][1] = 2      # error ofcourse : tuple inside tuple cannot be edited

exit()