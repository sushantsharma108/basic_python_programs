# lambda expression(anonymous function)-- Lambda expr. is a function which can be defined in only a line 
# but it doesn't contain any name.

# This is how we define function normally.
def add(a,b):
    return a+b

# This is how we define a functio with the help of Lambda expression.
add2 = lambda a,b: a+b # Now this function is defined & you can assign it to any variable and you can use 
                       # use that variable as a function call.
print(add2(2,3))  # Now this variable can be used as a function call and you can print the O/P 
# Actually we don't assign the lambda expr. into a variable but we are doing it since we uses them with the
# built-in-functions like map, reduce, filter in a program.

multiply = lambda a,b: a*b
print(multiply(2,3))   
# Now we are proving that these lambda expression(anonymous function) are anonymous meaning having no name.
print(add)
print(add2)
print(multiply)

# The O/P of above three lines 18,19,20 are showing that these functions are anonymous since in the memory 
# they aren't having name associated with them, they have only address in memory.