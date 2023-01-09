amnt = float(input("Enter the amount of money : "))

while amnt < 0:
     amnt = float(input("Please enter valid amount : "))

dot = str(amnt).find(".")
dlr = int(str(amnt)[:dot])
cnts = int(str(amnt)[dot+1:])

while cnts >= 100:
     cnts = cnts - 100
     dlr += 1

qtr = int(cnts/25)
cnts = cnts - (qtr*25)

dms = int(cnts/10)
cnts = cnts - (dms*10)

nckl = int(cnts/5)
cnts = cnts - (nckl*5)

pns = cnts

print("Dollars : {}\nQuarters : {}\nDimes : {}\nNickels : {}\nPennies : {}".format(str(dlr), str(qtr), str(dms), str(nckl), str(pns)))
