# def greater(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z: 
#         return y
#     else:
#         return z

# num1 = input("Enter No.1: ")
# num2 = input("Enter No.2: ")
# num3 = input("Enter No.3: ")
# print(f"The greatest of Three No.s is {greater(num1,num2,num3)}")

# PRINCIPLE OF PROGRAMMING: KISS --> "KEEP IT SIMPLE STUPID"

# Function inside another function
def greatest(a,b):
    if a>b:
        return a
    else:
        return b

# num1 = input("Enter No.1: ")
# num2 = input("Enter No.2: ")
# num3 = input("Enter No.3: ")
# print(f"The greatest of Three No.s is {greatest(greatest(num1,num2),num3)}")
# The above line shows the greater of three no.s

def new_greatest(a,b,c):
    bigger = greatest(a,b)
    return greatest(bigger,c)

print(new_greatest(10,20,15))



