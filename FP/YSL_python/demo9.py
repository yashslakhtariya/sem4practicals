class Haribol:
     mala = 16;
     
     @staticmethod
     def greet():
          print("Hare Krishna! All Glories to Srila Prabhupada!")
          # This static method can be created which doesn't require any self (here haribol) parameter
          # It can be called via object also and class also
     
     # Constructor called during object creation first
     def __init__(haribol, name):
          haribol.name = name
     
     def readSPbooks(haribol):
          print(f"{haribol.name} is reading SP books {haribol.hours} hour/s everyday")

Haribol.greet()     
ysl = Haribol("YSL")
ysl.mala = 18

print(f"YSL chants {ysl.mala} rounds")
print(f"Haribol should chant at least {Haribol.mala} rounds")

Haribol.mala = 64
ysl = Haribol("YSL")

print(f"YSL chants {ysl.mala} rounds")
print(f"Haribol should chant at least {Haribol.mala} rounds")

yash = Haribol("Yash")
yash.hours = 1

yash.readSPbooks()
# While calling method of class via object, actual code running is : 
Haribol.readSPbooks(yash)
yash.greet()
