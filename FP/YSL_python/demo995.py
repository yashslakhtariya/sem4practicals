# Map, Filter and Reduce


# Map

def addzero(n):
     return n+0
lst = [16, 32, 64]

print(tuple(map(addzero, lst)))


# Filter

def validMala(mala):
     if mala >= 16:
          return True
          # print(f"Haribol! Nice to hear, you chant {mala} rounds of Hare Krishna Mahamantra!")
     else:
          return False
          # print("O Krishna! You aren't even chanting 16 rounds of Hare Krishna Mahamantra!\nNoone can save you now!")

lst2 = [8, 16, 32, 64]
print(tuple(filter(validMala, lst2)))


# Reduce

from functools import reduce

sum = lambda y1, y2 : y1 + y2

lst3 = [16, 32, 64]
mala = reduce(sum, lst3)
print(mala)
