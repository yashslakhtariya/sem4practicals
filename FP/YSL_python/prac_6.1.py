import random

cages = []
for i in range(0, 50):
    k = random.randint(1, 100)
    cages.append(k)


def forLion(cages):
    if cages.__contains__(1):
        lion = cages.index(1)
        return cages, f"The cage number where Lion is kept is : {lion + 1}"
    elif not cages.__contains__(1):
        l = random.randint(0, 49)
        cages[l] = 1
        return cages, f"The cage number where Lion is kept is : {l + 1}"


print(f"\nCages with number of animals : {forLion(cages)[0]}\n\n{forLion(cages)[1]}")
