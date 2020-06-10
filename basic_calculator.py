# A BASIC CALCULATOR TO PERFORM SOME OPS.
print("Choose values from the options: ")
print("1.  Add")
print("2.  Subtract")
print("3.  Multiply")
print("4.  Divide")
num = int(input())
n1 = int(input("Enter 1st Num:"))
n2 = int(input("Enter 2st Num:"))

if num == 1:
    n3 = n1 + n2
    print(f"Your Addition is: {n3}")

elif num == 2:
    n3 = n1 - n2
    print(f"Your Subtraction is: {n3}")

elif num == 3:
    n3 = n1 * n2
    print(f"Your Multiplication is: {n3}")

elif num == 4:
    n3 = n1 / n2
    print(f"Your Division is: {n3}")

elif num > 4:
    print("Invalid Input...")

