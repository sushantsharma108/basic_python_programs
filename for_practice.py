num = input("Enter the no: ") #Don't change the input into the integer since we want to 
total = 0                       #work with the indexes of the string.
for i in range(0,len(num)):    
    total += int(num[i])     # It calculates the sum of no. upto the last index.
print(f"Total is {total}")

