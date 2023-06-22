from math import sqrt
print ("This code is written by \nMichael Perry Tettey")
print ("This Program is To Calculate The Variance and Standard Deviation of a Set of Numbers")
dataType = input ("Does your data contain frequencies, Y/N\n")
if (dataType == "Y"):
    X, f = [float(x) for x in input("Enter your x-Values: ").split(",")], [float(x) for x in input("Enter the frequency for each x-Value: ").split(",")]
    mean = sum(x*f for x, f in zip(X, f))/sum(f)
    print ("Mean is " + str(mean) )
    meanDeviation = [x - mean for x in X]
    print ("The Mean Devaitions are: ", str(meanDeviation))
    absoluteMeanDeviation= [x**2 for x in meanDeviation]
    print ("The square of Mean Deviations are: ", str(absoluteMeanDeviation))
    popuSamp = input ("Do you want to calculate Popoulation Variance (P) or Sample Variance(S). P/S \n")
    if (popuSamp == "P"):
        variance = sum(absoluteMeanDeviation)/sum(f)
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)
    elif (popuSamp == "S"):
        variance = sum(absoluteMeanDeviation)/(sum(f) - 1)
        print ("The variance is: ", float(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", float(standardDeviation))
elif (dataType == "N"):
    X = [float(x) for x in input("Enter your x-Values: ").split(",")]
    count = len(X)
    mean = sum(X)/count
    print ("Mean is ", + mean)
    meanDeviaton = [x - mean for x in X]
    absoluteSquareMeanDeviation = [x**2 for x in meanDeviaton]
    popuSamp = input ("Do you want to calculate Popoulation Variance (P) or Sample Variance(S). P/S \n")
    if (popuSamp == "P"):
        variance = sum(absoluteSquareMeanDeviation)/count
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)
    elif (popuSamp == "s"):
        variance = sum(absoluteSquareMeanDeviation)/(count - 1)
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)
