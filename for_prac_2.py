# input the user name and count the no. of times of each character comes into a string.

name = input("Enter Your Name: ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
    