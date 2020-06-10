def common_value(list1,list2):
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
    return common_list
num1 = [1,3,8,9]
num2 = [5,4,3,1]
print(common_value(num1,num2))  #print(common_value([1,3,8,9],[5,4,3,1])) ye bhi correct h

# Logic ye h ki hum sirf ek list me hee loop ko chalayenge aur uske baad if se check karenge ki loop ne jo element read kiya, kya wo 
# list 2 me bhi h ya nahi,Aur agar hua to use common_list me append kar denge. 