ysl = input("Enter a statement : ")
alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
ysl = ysl.lower()
for i in ysl:
    if i in alpha:
        alpha.remove(i)

if len(alpha) == 0:
    print("\n\tThe statement given is pangram!")
else:
    print("\n\tThe statement given is not a pangram!")
