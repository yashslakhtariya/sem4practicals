from YSL_io import *

class BnkAc:
     def __init__(self, name, ac, blnc):
          self.name = name
          self.ac = ac
          self.blnc = blnc
          self.min_blnc = 1000
          
          if self.blnc < self.min_blnc:
               raise ValueError(f"Minimum Balance of Rs.{self.min_blnc} required")
    
     @property
     def get_blnc(self):
          printGRN(f'\nBalance : Rs.{self.blnc}')
    
     def set_blnc(self, setblnc):
          if setblnc < self.min_blnc:
               raise ValueError(f"Minimum Balance of Rs.{self.min_blnc} required")
          else:
               self.blnc = setblnc
               printBLU(f"\nBalance set : Rs.{self.blnc}")
          
     def deposit(self, amount):
          self.blnc += amount
          printGRN(f'\nDeposited : Rs.{amount}\nCurrent Balance : Rs.{self.blnc}')
          
     def withdraw(self, amount):
          if self.blnc - amount < self.min_blnc:
               raise ValueError(f"Minimum Balance of Rs.{self.min_blnc} required")
          else:
               self.blnc -= amount
               printMGNTA(f"\nWithdrawn : Rs.{amount}\nCurrent Balance : Rs.{self.blnc}")
          
     def __str__(self):
          return f"\nAccount Holder : {self.name}\nAccount Type : {self.ac}\nBalance : Rs.{self.blnc}"
   
ysl = BnkAc('YSL', 'Savings', 64321616)
dpst = inputRED('\nEnter amount to deposit : ')
ysl.deposit(int(dpst))
wthdrw = inputRED('\nEnter amount to withdraw : ')
ysl.withdraw(int(wthdrw))
ysl.get_blnc
ysl.set_blnc(6464323216)
print(str(ysl))
