# in keyword and iterations in a dictionary
user_info = {
    'name' :'sushant',
    'age' : 22,
    'fav_movies' : ['stk','titanic','gatsby'],
    'fav_songs' : ['laal ishq','ritviz_songs']
}
# Check if key exist in dictionary: we'll use "in" keyword but it checks for only keys in a dictionary. 
if 'name' in user_info:
    print("present")
else:
    print("not present")    

if 'names' in user_info:
    print("present")
else:
    print("not present")    

# Check if the value exists in a dictionary: 
if 'sushant' in user_info.values():
    print('Present')
else:
    print('Not Present')

if 22 in user_info.values(): #jo 22 value h vo int h string nhi h, agar hum us int value ko str banakar chk karenge to not
    print('Present')           # present dega.
else:
    print('Not Present')
 

if '22' in user_info.values(): #jo 22 value h vo int h string nhi h, agar hum us int value ko str banakar chk karenge to not
    print('Present')           # present dega.
else:
    print('Not Present')
 
# If we wanna check that a list is present in or not in a dict.:
if ['stk','titanic','gatsby'] in user_info.values():
    print('Present')
else:
    print('Not Present')
