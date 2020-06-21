# The below 4 stmts. are used to input data from the user.
user_data = {}  #This is an empty dictionary.
name = input('What"s your name ?: ')
age = input('What"s your age ?: ')
fav_movies = input('What are your favourite movies ?: ').split(',')
fav_songs = input('What are your favourite songs ?: ').split(',')

# Now we are adding the input data into our dictionary.
user_data['name'] = name
user_data['age'] = age
user_data['favourite movies'] = fav_movies
user_data['favourite songs'] = fav_songs

for key,value in user_data.items():
    print(f"{key}:{value}")



