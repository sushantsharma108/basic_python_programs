# Default Parameters:

# def user_info(f_name,l_name,age):         # This function has not any default arguments.
#     print(f"Your First Name is {f_name}")
#     print(f"Your Last Name is {l_name}")
#     print(f"Your Age is {age}")
# print(user_info("Sushant","Sharma",22))

# def user_info(f_name,l_name,age = 22):    # In this line the age=22 is a default argument.
#     print(f"Your First Name is {f_name}")       #In this func. we can make f_name & l_name default arguments
#     print(f"Your Last Name is {l_name}")            #by providing them values like None & unknown.
#     print(f"Your Age is {age}")
# print(user_info("Sushant","Sharma"))

def user_info(f_name = 'unknown', l_name = 'unknown', age = None):    # In this line the age=None is a default argument.
    print(f"Your First Name is {f_name}")       #In this func. we can make f_name & l_name default arguments
    print(f"Your Last Name is {l_name}")            #by providing them values like None & unknown.
    print(f"Your Age is {age}")
print(user_info())


    