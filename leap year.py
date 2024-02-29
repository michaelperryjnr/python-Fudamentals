#allow user to input year 
print("Hey there don't forget to star and contribute")
year = int (input("Input a year\n"))


#function to check the year by modulus 
if (year % 4 == 0):
    print ("The Year ", year , "is a leap year")
else:
    print ("The Year",year, "is not a leap year")
