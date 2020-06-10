# numbers = [1,2,3,4,5,6,7,8,9,10]  #Here the list is passed by the programmer

def square_list(l):  # This func. gives the square of numbers defined in a list.
    square = []
    for i in l:
        square.append(i*i)
    return square
numbers = list(range(1,11))  # Range() function is used to generate list also & also used in for loop.
print(square_list(numbers))


