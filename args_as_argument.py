# This is a program which illustrates  that how we can pass a list of elements and how they are multiplied 
# instead of multiplication of a whole list with the multiply variable. 

def multiply_nums(*args):
    multiply = 1
    print(args) # ([]) At this point the *args cease to work & the whole list is multiplied by 1. 
    for i in args:
        multiply *= i
    return multiply

nums = [2,3,4]  # can also use a tuple (2,3,4)
print(multiply_nums(2,3))
# print(multiply_nums(nums)) This will give an error.
print(multiply_nums(*nums))
#At this point nums which is a list is treated as a single argument
# In the line 10 that's an error which is solved by writing *nums in function call which unpacked all
# all the elements of a list and it's multiplied by 1. 

# And in the program lines above you can also provide a 'tuple' instead of a 'list' which is also correct.
