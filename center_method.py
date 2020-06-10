# center(): this method is used to add any special characters on both sides  of the string.

name = "Sushant"

# To add the special character on both the sides of string we use center() method which 
# use the no. of counts of spec. char.

print(name.center(7+4,"*"))     # 7 is len() of string & 4 is the no. of count of asterisks to be added(2 on both sides)
                                # We can pass any special char. but it must be of only length 1.
                                # To use the center method we must knnow the length of the string.

print(name.center(7+4,"_"))
print(name.center(7+3,"*"))
print(name.center(7+2,"*"))
print(name.center(7+1,"*"))
print(name.center(7+0,"*"))

name1 = input("enter your name: ")
length = print(name1.center(len(name1) + 6,"*"))   #This line adds the required no. of spec char on both sides of string.