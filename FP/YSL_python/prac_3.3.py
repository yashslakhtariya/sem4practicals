import time

q1 = ["What is Linux natively",
      "Which is most used basic shell in Linux distros",
      "Which linux command is used to manage processes",
      "Which is the most popular community driven linux distribution",
      "Which package manager Arch based distributions use"]
q2 = ["Which is the most popular Linux desktop environment",
      "Which display protocol is newer and tends to replace X server",
      "RHEL is derived from which linux distribution",
      "Fedora uses a package manager which is slower compared to others. Which is it",
      "Which linux command is used to do an activity as root"]

a1 = ["kernel", "bash", "top", "arch", "pacman"]
a2 = ["gnome", "wayland", "fedora", "dnf", "sudo"]


def linuxquiz1(stdnt_name: str):
    ans = ["", "", "", "", ""]
    mrks = 0
    print("\n\tLinux Quiz 1!")
    begin = time.time()

    for i in range(0, len(q1)):
        print(f"\n{q1[i]}?")
        ans[i] = input("Answer : ").lower()
        if str(ans[i]).__contains__(str(a1[i])):
            mrks += 1
    end = time.time()

    print(f"\nIn Linux Quiz 1, the score of the student {stdnt_name} is : {mrks} marks\nThe records are : ")
    for i in range(0, len(q1)):
        print(f"\n\t{q1[i]}?\n\tAnswer given : {ans[i]}\n\tCorrect answer : {a1[i]}")
    print("\nTime taken for quiz : {:.4f} minutes".format((end - begin)/60))


def linuxquiz2(stdnt_name: str):
    ans = ["", "", "", "", ""]
    mrks = 0
    print("\n\tLinux Quiz 2!")
    begin = time.time()

    for i in range(0, len(q2)):
        print(f"\n{q2[i]}?")
        ans[i] = input("Answer : ").lower()
        if str(ans[i]).__contains__(str(a2[i])):
            mrks += 1
    end = time.time()

    print(f"\nIn Linux Quiz 2, the score of the student {stdnt_name} is : {mrks} marks\nThe records are : ")
    for i in range(0, len(q2)):
        print(f"\n\t{q2[i]}?\n\tAnswer given : {ans[i]}\n\tCorrect answer : {a2[i]}")
    print("\nTime taken for quiz : {:.4f} minutes".format((end - begin)/60))


stdnt_name = input("Enter the name of student : ")
choice = input("Enter which Linux Quiz to take? (1 or 2) : ")
while choice != "1" and choice != "2":
    print("Invalid Input!")
    choice = int(input("Enter which Linux Quiz to take? (1 or 2) : "))

if choice == "1":
    linuxquiz1(stdnt_name)
elif choice == "2":
    linuxquiz2(stdnt_name)
