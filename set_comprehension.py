# This program illustrates the set comprehension
sets = {k**2 for k in range(1,11)}
print(sets)

strings= ['Sushant','Yash','Shubham','Tushar']
first = {i[0] for i in strings}
print(first)
