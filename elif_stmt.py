# Use of elif stmt. through Ticket Selling System.
# if age is:
# b/w 1 to 3 then ticket is free
# b/w 4 to 10 then ticket is 150 
# b/w 11 to 60then ticket is 250
# above 60 then ticket is 200

age = int(input("Enter Your Age: "))
if age==0 or age<0:
    print("You Can't Watch The Movie.")
elif 0<=age<=3:
    print("Your Ticket is Free. ")
elif 4<=age<=10:
    print("Your Ticket is For Rs.150")
elif 11<=age<=60:
    print("Your Ticket is For Rs.250")
else:
    print("Your Ticket is For Rs.200")
        

