def filter_odd_even(l):  #This func. will filter out even & odd no.s from a list of given numbers.
    odd_nums = []  # List to store odd no.s
    even_nums = []  #List to store even no.s
    for i in l:
        if i%2 == 0:  # Checks whether a no. is even or not
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums, even_nums]  # No.s will come in the form of list within list. If you will use '+' sign instead of commma then the two 
    return output                   # will add or concatenate to form a single list.

numbers = [1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(numbers))  # Func. call.