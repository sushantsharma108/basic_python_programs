# # functions are useful in solving real world problems
# #  with the help of functions, we don't have to repeat the code.
# # name = "Sushant   "  # len() func. also count the spaces in a string.
# # print(len(name))

# # For example if you want to define the function to add the two no.s.

# # Function Syntax: def func_name()
def add_two(a,b):             # def keyword is used for function definition.
    return a+b                  #a,b are the parameters of a function or the inputs passed to the func.
#in place of  return we can also write print(parameters)     #return keyword returns the value evaluated by the function.

# total = add_two(5,4)
# print(total)            #Stmt 13 & 14 both are same.
# print(add_two(5,4))     # in this stmt we called the function & passed the value and
#                          # At this point the print() evaluates the function call. 

# num1,num2 = input("Enter two no.s: ").split(',')
# total_sum = add_two(int(num1),int(num2))
# print(total_sum)

# Func. to concatenate two strings.

f_name,l_name = input("Enter the First & Last Name: ").split(" ")
print(f"The Complete name is: {add_two(f_name,l_name)}")




