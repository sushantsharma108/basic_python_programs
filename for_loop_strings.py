# name = "Sushant" 
# for i in range(len(name)):
#     print(name[i])
#  The abbove code is applicable in python, java, js , etc...

# Now this code is applicable to only Python & it is optimized.
name = "Sushant"
for i in name:          #In place of name we acn also put a string.like for i in "Sushant"
    print(i)

# For the sum of digits in a no.
num = input("Enter a no: ")
total = 0
for i in num:
    total += int(i)
print(total)
