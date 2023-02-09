class Train:
     
     train: str
     seats: int
     
     def __init__(self, train, seats):
          self.train = train
          self.seats = seats
     
     def getStatus(self):
          print(f"Number of available seats for train {self.train}: {self.seats}")
     
     @staticmethod
     def getFare():
          print("The fare per ticket is : Rs.10 per ticket")
          
     def bookTicket(self, n: int):
          self.seats = self.seats - 1
          print(f"Ticket Price : Rs.10 per ticket\nPrice to pay for {str(n)} tickets : {n * 10}")
          y = input("Do you want to book the ticket? : ")
          y = str(y.lower())
          if y.__contains__("yes"):
               print("Your ticket is booked successfully!\nThank you!")
          elif y.__contains__("no"):
               print("Sorry! Your ticket is not booked\nThank you!")
          else:
               print("Invalid Input!")
    
t1 = Train("T643216", 1728)
t2 = Train("T163264", 108)

t1.getStatus()
t1.getFare()
t1.bookTicket(32)

print("\n")

t2.getStatus()
t2.getFare()
t2.bookTicket(16)
