user_info = {
    'name' :'sushant',
    'age' : 22,
    'fav_movies' : ['stk','titanic','gatsby'],
    'fav_songs' : ['laal ishq','ritviz_songs']
}
# # Add data to a dictionary:
user_info['products'] = ['fan','lights','motors']  # By default tuple will form not lists.
print(user_info)

# # pop() method to remove any key: value pairs:
popped_item = user_info.pop('fav_songs')  #Pop() method me aapko at least ek argument to pass krna hi hoga warna error aayega
print(popped_item)
print(user_info)

# popitem() method: This method will automatically deletes a random key:value pair in a dictionary.
popped_item1 = user_info.popitem()  #No need to pass any argument in this method
print(user_info)
print(popped_item1)





