from YSL_io import *

class Stack:
     
     def __init__(self, l1=[]):
          self.stck = l1
          
     def Push(self, y):
          try:
               self.stck.append(y)
          except:
               printRED('Something went wrong!')
          else:
               print(y, end=' ')
               printGRN('pushed to the stack')
               self.Display()
          
     def Pop(self):
          try:
               y = self.stck.pop()
          except:
               printRED('Something went wrong!')
          else:
               print(y, end=' ')
               printORNG('popped from the stack')
               self.Display() 
                     
     def Peek(self):
          print(self.stck[-1], end=' ')
          printBLU('is at top of the stack')
          self.Display()
          
     def Display(self):
          printMGNTA('Stack', end=' : ')
          print(f'{self.stck}\n')

          
s = Stack([1, 2, 3])
s.Push(64)
s.Peek()
s.Pop()