import string


def bnkusr():
    print("\n\tWelcome to Kadi Nagarik Sahakari Bank Limited!\n")
    name = input("Enter your name : ")
    for i in name:
        while i not in string.ascii_letters + " ":
            name = input("Please enter valid name : ")

    addr: str = input("Enter your address : ")

    cntct = input("Enter your contact : ")
    while len(cntct) != 10 or not cntct.isdigit():
        cntct = input("Enter your valid contact : ")
    cntct = int(cntct)

    pin = input("Enter your pincode : ")
    while len(pin) != 6 or not pin.isdigit():
        pin = input("Enter your valid pincode : ")
    pin = int(pin)

    hbs: str = input("Enter your hobbies : ")

    goal: str = input("Enter your Life goal : ")

    age = int(input("Enter your age : "))
    while age < 0:
        age = int(input("Enter your valid age : "))

    return name, cntct, addr, age, hbs, goal


def schemes(name, cntct, addr, age, hbs, goal):
    if age <= 12:
        scheme = "You are eligible for Educational Camp Schemes : https://www.india.gov.in/people-groups/life-cycle/kids"
    elif age <= 19 and age > 12:
        scheme = "You are eligible for Educational Scholarship Schemes : https://www.aicte-india.org/schemes/students-development-schemes"
    else:
        scheme = "You are eligible for Retirement Plans : https://www.policybazaar.com/life-insurance/pension-plans/"

    return name, cntct, addr, age, scheme, hbs, goal


def setDetails():
    n = int(input("Enter how many person want to register : "))
    details = {}
    users = []
    for i in range(n):
        name, cntct, addr, age, hbs, goal = bnkusr()
        name1, cntct1, addr1, age1, scheme1, hbs1, goal1 = schemes(name, cntct, addr, age, hbs, goal)
        details["Name"] = name1
        details["Age"] = age1
        details["Contact"] = cntct1
        details["Address"] = addr1
        details["Hobbies"] = hbs1
        details["Life Goal"] = goal1
        details["Scheme"] = scheme1
        users.append(details)
        i = i + 1
    return users


def getDetails(users: list):
    print("\n")
    for i in range(len(users)):
        for k, v in users[i].items():
            print(f"{k} : {v}")
    i = i + 1


users = setDetails()
getDetails(users)
