import string


def bnkusr():
    print("\n\tWelcome to Kadi Nagarik Sahakari Bank Limited!")
    name = input("Enter your name : ")
    for i in name:
        while i not in string.ascii_letters + " ":
            name = input("Please enter valid name : ")


bnkusr()
