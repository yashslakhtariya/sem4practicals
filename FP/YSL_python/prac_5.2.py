def bblesrt(ysl: list):
    for i in range(len(ysl) - 1):
        for j in range(len(ysl) - i - 1):
            if ysl[j] > ysl[j + 1]:
                ysl[j], ysl[j + 1] = ysl[j + 1], ysl[j]


ysl_lst = [64, 16, 32, 22, 28, 18, 24, 20]
bblesrt(ysl_lst)
print(ysl_lst)
