# fromkeys method:
# d = {'name':'unknnown','age':'unknown'}  #ab agar aapki dict me kaafi values h jo ki by default unknown honi chahiye to aap is line ki
# tarah  bhi define kr skte h otherwise fromkeys() method ka bhi use kr skte hain.
d = dict.fromkeys(['name','age','place','height'],'unknown') #This method will make all values unknown or as you will define in fromkeys
# method
print(d)
d = dict.fromkeys(('name','age','place','height'),'unknown') # We can also define a tuple
print(d)
d = dict.fromkeys("abc",'unknown') # In this case the a,b, and c will become individual keys.
print(d)
d = dict.fromkeys(range(1,6),'unknown')
print(d)
d = dict.fromkeys(['name','age'],['unknown','unknown'])   # In this case the value of var. name & age will become [unknown,unknown]
print(d)

# get() method (very useful)
d1 = {'name':'Sushant Sharma Ji','age': 23,'address':'New Delhi'}
print(d1['address'])
# Bit if I access a key which is not in my dict. then compiler will give an error.
# print(d1['addresses']) # THIS WILL GIVE AN ERROR
# If we wanna handle these errors then we use the get() method.
print(d1.get('name'))
print(d1.get('names')) # This haven't given any error since the get() method returns 'None' if that key or value is not present in our dict.
# The above get() method is very useful & much better to access your leys in a dictionary.

# if 'name' in d1:
#     print('present')
# else:
#     print('not present')

# The below method is also used to check or access your key in a dict.
if d1.get('name'):
    print('Present')
else:
    print('not present')

# CLEAR METHOD.
# d1.clear() # It will clear or empty your dictionary.
# print(d1)  

# COPY METHOD
d2 = d1.copy()
print(d2)

d2 = d1 # This doesn't make any copy but d2 and d1 both are same dictionary. You can work with either of them. and changes occur in one dict. 
#  also reflects in other dictionary.
d1.popitem()
print(d1)
print(d2)

print(d2 is d1) # This line will ensure that the d2 and d1 are in the same memory location.
print(d2 == d1) # This line will compare the values of both the dicts. and if value are same then it will return True.
  


