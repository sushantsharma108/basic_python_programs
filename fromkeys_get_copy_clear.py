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
