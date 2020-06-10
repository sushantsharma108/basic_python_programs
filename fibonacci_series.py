# Fibonacci Series:
# 0,1,1,2,3,5,8,13,21.......
# If user wants to print 'n' no. in Fibonacci Series then:
# 1 no: 0
# 2 no.s: 0 1
# 3 no.s: 0 1 1
# n no.s: 0 1 1 2......n-2

# for i in range(1,11):
#     print(i, end=" ")   # This line prints the no. on the same line not in the next line.
#                         # The ouput in print stmt can also be , or space separated.like.
     
def fibonacci_seq(n):
    a = 0 # First Number
    b = 1 # Second Number
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)  # a b, 
    else:
        print(a, b,end= " ")
        for i in range(n-2):
            c = a+b  # c=1
            a = b
            b = c
            print(b, end=" ")
print(fibonacci_seq(10)) 