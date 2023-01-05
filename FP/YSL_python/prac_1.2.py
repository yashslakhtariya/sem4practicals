import datetime

print("\n\t\tRegistration Form for online game competition\n")

teamornot = int(input("Individual Application(type 1) or Team Application(type 2)? \n"))

if teamornot == 1:
    name = str(input("Name : "))

    age = int(input("Age : "))
    while age < 12 or age > 100:
        age = int(input("Please input valid age between 12 and 100 : "))

    contact = int(input("Contact : "))
    while len(str(contact)) != 10:
        contact = int(input("Valid Contact : "))

    nofgms = int(input("Enter number of games you want to participate : "))
    games = []
    for i in range(0, nofgms):
        g = input('Game {} : '.format(i+1))
        games.append(g)
    timenow = datetime.datetime.now()

    print("\n\tDetails given : \n")
    print("Name - {}".format(name))
    print("Age - {}".format(age))
    print("Contact - {}".format(contact))
    for i in range(0, nofgms):
        print("Game {0} - {1}".format(i+1, games[i]))
    print("Timestamp of filling form : {0}".format(timenow))

elif teamornot == 2:
    nofmbrs = int(input("Enter number of members in the team : "))

    lname = str(input("Leader Name : "))
    mbrname = [{'Leader Name': lname}]
    for i in range(0, nofmbrs-1):
        m = input("Name of Member {} : ".format(i+1))
        mbrname.append({'Member {} Name'.format(i+1): m})

    lage = int(input("\nLeader Age : "))
    while lage < 12 or lage > 100:
        lage = int(input("Valid Leader Age between 12 and 100 : "))
    mbrage = [{'Leader Age': lage}]
    for i in range(0, nofmbrs-1):
        a = int(input('Member {} Age : '.format(i+1)))
        while a < 12 or a > 100:
            a = int(input('Valid Age of Member {} : '.format(i+1)))
        mbrage.append({'Member {} Age'.format(i+1): str(a)})

    lcontact = int(input("\nLeader Contact : "))
    while len(str(lcontact)) != 10:
        lcontact = int(input("Valid Leader Contact : "))
    mbrcontact = [{'Leader Contact': str(lcontact)}]
    for i in range(0, nofmbrs-1):
        c = int(input("Member {} Contact : ".format(i+1)))
        while len(str(c)) != 10:
            c = int(input("Valid Member {} Contact : ".format(i+1)))
        mbrcontact.append({"Member {} contact".format(i+1): str(c)})

    nofgms = int(input("\nEnter number of games you want to participate : "))
    games = [{}]
    for i in range(0, nofgms):
        g = str(input('Game {} : '.format(i+1)))
        games.append({"Game {}".format(i+1): g})
    timenow = datetime.datetime.now()

    print("\n\tDetails given : \n")
    for i in range(0, nofmbrs):
        print(str(mbrname[i]).replace("'", "").replace("{", "").replace("}", "").replace(":", " -"))
        print(str(mbrage[i]).replace("'", "").replace("{", "").replace("}", "").replace(":", " -"))
        print(str(mbrcontact[i]).replace("'", "").replace("{", "").replace("}", "").replace(":", " -"))
        print("\n")
    for i in range(1, nofgms+1):
        print(str(games[i]).replace("'", "").replace("{", "").replace("}", "").replace(":", " -"))
    print("Timestamp of filling form : {0}".format(timenow))
else:
    print("Invalid Input!")
