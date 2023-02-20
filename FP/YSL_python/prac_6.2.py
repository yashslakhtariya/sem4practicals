ysl = input("Enter any paragraph : ")
ysl = ysl.lower().replace(" ", "")
cnt = dict()

for c in ysl:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

print(f"\nThe number of occurrence of all characters (case insensitive) in the given text : \n")
for c in cnt:
    print(f"\t{c} : {cnt[c]}")
