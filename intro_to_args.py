# args is used to make the flexible functions.
#  *operator
#  *args
def total(a,b):
    return a+b # It's a function which gives the sum of only two numbers, but if you passes more than 2 arguments then 
               # it will give an error.

# def all_total(*args):  # This line of code will not give any error but it gives the sum of any amount of numbers.
#     print(args)        # and here the args is not a keyword, you can write any words on the place of args but 
#     print(type(args))  # conventionally you should write args and here all work is doing by * operator.

# The above line with no.9  converts all numbers into a tuple with individual numbers.
def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4,5,6))