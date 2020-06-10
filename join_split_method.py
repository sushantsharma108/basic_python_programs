# split method: converts the string to list.
# user_info = "Sushant 22"
# print(user_info.split())

# name,age = input("Enter your name & age: ").split(",")
# print(f"Your name & age is {name},{age}")

# Join method: converts lists to string. It only works on the string items in the list.
user_info = ['Sushant','Sharma','22']
print(','.join(user_info))  #First value in print func. is that value with which you want to separate 
                            # your data in a list.