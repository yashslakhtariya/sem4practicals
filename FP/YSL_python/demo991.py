def greet(name: str):
     print(f'Hare Krishna {name.capitalize()}')
     
print(__name__) # output : main
     
if __name__ == "__main__":
     n = input("Enter your name : ")
     greet(n)
