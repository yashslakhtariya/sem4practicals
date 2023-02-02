def score(score):
    fl = open("demofile.txt", "r")
    tmp = fl.read()
    tmp1 = tmp[-1]
    tmp2 = tmp[-2]
    mala = int(tmp2 + tmp1)
    fl.close()
    fl = open("demofile.txt", "w")
    if int(score) > mala:
        fl.write(f"You are chanting rounds = {score}")
    fl.close()


with open("demofile.txt", 'w') as f:
    f.write("You are chanting rounds = 00")

score(16)
