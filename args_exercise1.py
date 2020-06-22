# This program illustrates that how a user can pass a list or tuple to a function as args
# and the function will return a list in which each element is powered upto any number (square,cube,etc... of elements).
def to_power(num,*args):
    if args:   # This line will check that the user has passed the arguments or not means if args is empty or not.If its not
        return [i**num for i in nums]  #empty then func. returns a list...
    else:
        return "Hey, you didn't pass any args..."
    
m = int(input("Enter a num"))
nums = [1,2,3]
print(to_power(m,*nums))   # You can also pass the argument as a list or tuple or variable in which list or tuple is stored.



    
