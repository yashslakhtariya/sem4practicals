import random

base = random.randint(1, 10)
power = random.randint(1, 5)

n = base ** power
y = input(f"\n\tFill in the blanks : {base}^__ = {n}\n\tAnswer : ")
while not y.isdigit():
    print("Invalid Input! Please enter a valid digit!")
    y = input(f"\n\tFill in the blanks : {base}^__ = {n}\n\tAnswer : ")
y = int(y)
if y == power:
    print("\n\tGreat! Your answer is absolutely correct!")
else:
    print(f"\n\tAlas! Your answer isn\'t correct this time!\n\tCorrect answer is {power}")
