from YSL_io import *

class Complex:
    def __init__(self, real, img=3):
        self.real = real
        self.img = img
        
    def __add__(self, other):
        print(f"Addition of {self} and {other} : ", end=' ')
        printORNG(f'{self.real + other.real} + {self.img + other.img}i')
    
    def __sub__(self, other):
        print(f"Subtraction of {self} and {other} : ", end=' ')
        printORNG(f'{self.real - other.real} + {self.img - other.img}i')
    
    def __mul__(self, other):
        result_real = self.real * other.real - self.img * other.img
        result_img = self.real * other.img + self.img * other.real
        if result_real == 0 and result_img == 0:
            raise ValueError("Multiplication result cannot be zero")
        print(f"Multiplication of {self} and {other} : ", end=' ')
        printORNG(f'{result_real} + {result_img}i')
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

c1 = Complex(2, 4)
c2 = Complex(1, 2)

c1 + c2
c1 - c2
c1 * c2
