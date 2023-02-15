# Super keyword

class Dashrath:
     name = "King Dashratha"
     
     def __init__(self):
          print("King Dashratha")
          
     def dtls(self):
          print("King Dashratha was the father of Lord Ramachandra")
          
class Rama(Dashrath):
     name = "Lord Ramachandra"
     
     def __init__(self):
          super().__init__()
          print("Lord Ramachandra")
          
     def Details(self):
          print("Lord Ramachandra is Maryada-Purushottama")
          
class Luv(Rama):
     name = "Luv"
     
     def __init__(self):
          print("Luv")
          
     def details(self):
          super().dtls()
          print("Luv was the son of Lord Ramachandra")
          
d = Dashrath()
r = Rama()
l = Luv()

print("===============================================================")
d.dtls()
print("===============================================================")
r.Details()
print("===============================================================")
l.details()
print("===============================================================")
