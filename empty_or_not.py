#Check whether a string is Empty or Not. Very Very important.

name = "Sushant"    # Since the string is not empty i.e name = "" --> Empty String.
if name:            #This condition will Check whether a string is Empty or Not.
    print("String is not empty.")
else:
    print("String is Empty.")


name1 = ""
if name1:            #This condition will Check whether a string is Empty or Not.
    print("String is not empty.")
else:
    print("String is Empty.")

name2 = input("Enter your Name: ")  # This line will check that the user did enter his name or not.
if name2:
    print(f"Your name is {name2}")
else:
    print("You didn't enter anything.")

