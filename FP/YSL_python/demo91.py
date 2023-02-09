class Programmer:
     name: str
     email: str
     number: int
     company = "BBT"
     
     def __init__(self, name: str, email: str, number: int):
          self.name = name
          self.email = email
          self.number = number
          
     def show(self):
          print(f"\n\tEmployee Details of {self.company} : \n\nName : {self.name}\nEmail : {self.email}\nMobile number : {str(self.number)}")
          
yash = Programmer("Yash S Lakhtariya","yashlakhtariya@protonmail.com",6351573711)
rishabh = Programmer("Rishabh S Maloo","rishabhmaloo392002@gmail.com",9998620417)

yash.show()
rishabh.show()
