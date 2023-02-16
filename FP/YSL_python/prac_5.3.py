def idntty(rows, cols, a):
    if rows != cols:
        return False
    else:
        for i in range(0, rows):
            for j in range(0, cols):
                if i == j and a[i][j] != 1:
                    return False
                elif i != j and a[i][j] != 0:
                    return False
                else:
                    return True


def bnry(rows, cols, a):
    for i in range(rows):
        for j in range(cols):
            if a[i][j] not in [0, 1]:
                return False
            return True


rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))
mat = [[i * j for i in range(rows)] for j in range(cols)]
for i in range(0, rows):
    for j in range(0, cols):
        mat[i][j] = int(input(f"Enter element a[{i}][{j}] : "))

print("\n\tThe Matrix is : \n")
for i in range(rows):
    for j in range(cols):
        print(mat[i][j], end=" ")
    print("")

if idntty(rows, cols, mat):
    print("\n\tYes, it is Identity Matrix")
else:
    print("\n\tNo, it is not Identity Matrix")

if bnry(rows, cols, mat):
    print("\n\tYes, it is Binary Matrix")
else:
    print("\n\tNo, it is not Binary Matrix")
