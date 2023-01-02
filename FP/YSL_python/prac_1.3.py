import random

num = random.randint(0,1000)
sum = 0
for i in str(num):
    sum += int(i)
print("The sum of digits of number {0} is {1}".format(num,sum))