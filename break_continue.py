# break and continue are the keywords
# break is used to break or for the termination of loop

# continue is used to continue the execution of stmts in a loop.
# we want to print numbers from 1 t0 10.
for i in range(1,11):
    if i == 5:
        break   #This line dbreks the loop when i became equal to 5.
    print(i)

# continue
# print no. from 1 to 10, but not 5
# 1,2,3,4,6,7,8,9,10

for i in range(1,11):
    if i == 5:
        continue   # When this stmt. will run then the program control returns back to the for loop line when it reaches to continue stmt.
    print(i)        # The line after continue will not execute.
#  We can use continue stmt to skip some things in programming.