user_info = {
    'name' :'sushant',
    'age' : 22,
    'fav_movies' : ['stk','titanic','gatsby'],
    'fav_songs' : ['laal ishq','ritviz_songs']
}
for i in user_info:  #It will print all the keys in a loop. 
    print(i)       

for i in user_info.values():  #It will print all the values in a loop. 
    print(i)       

# Values() method in a dictionary:
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# Keys() method in a dictionary:
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# items() method in a dictionary: this method will give keys & values of dict. in the form of tuples inside a list..
user_items = user_info.items()    # [('name','sushant,),('age',22),(),(),......]--> Output
print(user_items)
print(type(user_items))

for key,values in user_info.items():
    print(f"{key}:{values}")

