import random

r = random.randint(10, 99)

n = int(input("Enter a 2 digit number : "))

while n < 10 or n > 99:
    print("Invalid Input!")
    n = int(input("Please enter a valid 2 digit number : "))

n1 = int(n/10)
n2 = n % 10
r1 = int(r/10)
r2 = r % 10

print("Lottery number : {}".format(str(r)))

if n == r:
    print("Congratulations! You won $10000")

elif n1 == r2 and n2 == r1:
    print("Congratulations! You won $5000")

elif str(r).__contains__(str(n1)) or str(r).__contains__(str(n2)):
    print("Congratulations! You won $2000")

else:
    print("Sorry! Better luck next time!")
