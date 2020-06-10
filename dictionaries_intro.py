# Dictionaries Intro:
# Dictionaries ?
# A: we use dictionaries due to the limitations of lists,since lists are not enough to represent real world data.
# example:
# user = ['Sushant',22,['STK','Titanic'],['Mi Remix','Tandav Strot']]
# this user var. is a list which contain his name,age,fav movie,fav. ringtones....
# But this is not the best way to represent data since its not very clear.

# DICTIONARIES: Unordered collection of data in "Key:Value" Pair. "And most imp. thing is that dictionary doesn't have any index."
# represented by {}
user = {'name':'sushant','age':'24'}
print(user)
print(type(user))

# Second method to create a dictionary using dict():
user1 = dict(name = 'Sushant',age = 22)
print(user1)
print(type(user1))

# How to access data from the dictionary: dict_name['Key']
# Note: there is no indexing in dictionary because of unordered collection of data.
print(user['name'])
print(user['age'])

# Which type of data a dictionary can store: ANYTHING --> numbers,strings,lists,dictionary inside dictionary
user_info = {
    'name1' :'sushant',
    'age' : 22,
    'fav_movies' : ['stk','titanic','gatsby'],
    'fav_songs' : ['laal ishq','ritviz_songs']
}
print(user_info)
print(user_info['fav_movies'])

# HOW TO ADD DATA TO AN EMPTY DICTIONARY:
users_info = {}
users_info['name']='shubham'
users_info['place']='new delhi'
print(users_info)

