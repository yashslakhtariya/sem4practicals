def bblesrt(ysl: list):
    for i in range(len(ysl) - 1):
        for j in range(len(ysl) - i - 1):
            if ysl[j] > ysl[j + 1]:
                ysl[j], ysl[j + 1] = ysl[j + 1], ysl[j]


ysl_lst = []
print("\nEnter 10 elements to add in a list : ")
for i in range(0, 10):
    ysl_lst.append(int(input("")))
bblesrt(ysl_lst)
print(f"The sorted list is : {ysl_lst}")
