# *args with normal parameter

def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,2,3,4,5)) # You can define multiple parameters
# When function is called then value is called 'argument'
# When function is defined then value is called 'parameter'

def multiply_nums1(num, *args):
    multiply = 1              # Now in this case we defined a normal parameter 'num' but when we passes the actual arg. 
    for i in args:            # in func. call then the first value/arg. is passed in 'num' then the func call only 
        multiply *= i        # evaluates the multiplication of only other 4 value except 1.
    return multiply
print(multiply_nums1(5,2,3,4,5)) # Here the O/P should be 600 