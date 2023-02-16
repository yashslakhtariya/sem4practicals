# Operator overloading
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print(f"Addition = {self.num + other.num}")
        return self.num - other.num
    # it will return difference of numbers instead of addition when '+' operator is used

    def __str__(self):
        return f"Operator \'+\' is  overloaded"


n1 = Number(64)
n2 = Number(48)

sum = n1 + n2
print(sum)
print(str(n1))
