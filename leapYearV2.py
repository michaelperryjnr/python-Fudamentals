leapYear = int(input("Enter a year \n"))
if leapYear % 100 == 0 and leapYear % 400 == 0:
    print(leapYear, "is an end of century leap year")
elif leapYear % 100 != 0 and leapYear % 4 == 0:
    print(leapYear, "is a leap year")
else:
    print(leapYear, "is not a leap year")
