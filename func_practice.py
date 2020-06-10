# def char_return(a):
#     return a[-1]

# user_input = input("Enter Your Name: ")
# print(f"Last Character Of Your Name is: {char_return(user_input)}")

# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

#  We can even return a string in output

# def odd_even(num):
#     if num%2==0:
#         return "Even"    # In this code the else stmt is not mandatory. If the condition becomes True then if block will 
#     return "Odd"         # run otherwise it will return "Odd"

# def odd_even(num):
#     if num%2==0:
#         return "Even"
#     return "Odd"
# number = int(input("Enter a No: "))
# print(f"The No. Entered is {odd_even(number)}")


# Returning Boolean Values.
def odd_even(num):
    return num%2==0         #This function will Return Either True OR False.

print(odd_even(65))
# Mostly used Pythonic Way to define function

# Functions with no parameters and no arguments.
def song():
    return "Sushant's Favourite Song."
print(song())


