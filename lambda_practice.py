# lambda expression practice:
def is_even(a):
    if a%2 == 0:
        return True
    return False
# Above func. can also be written as:
def is_even1(a):
    return a%2 == 0   # Now this func. will also tell us that a no. is even or not by using Boolean Value.

print(is_even1(8))

# Now the above function is defined by using Lambda expression.
is_even2 = lambda a: a%2 == 0
print(is_even2(18))

# Now this is a function which will give the last character of a string which is defined normally.
def last_char(str):
    return str[-1]

# And now same function is defined by using lambda expression.
last_char1 = lambda string :string[-1]
print(last_char1("Sushant"))

# How to use if-else stmts. with Lambda Expressions.
def func(string):
    if len(string) > 5:
        return True
    return False

func2 = lambda string: True if len(string) > 5 else False
func3 = lambda string: len(string) > 5 # This line will produce the same O/P as the above line. 
print(func2("Sushant"))
print(func3("Sharma"))
