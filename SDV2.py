from math import sqrt
#This is just introductory
print ("This code is written by \nMichael Perry Tettey")
print ("This Program is To Calculate The Variance and Standard Deviation of a Set of Numbers")


#to check the type of dataset, grouped or ungrouped
dataType = input ("Does your data contain frequencies, Y/N\n")


#logic and logics for grouped data sets
if (dataType == "Y" or dataType == "y"):
    X, f = [float(x) for x in input("Enter your x-Values: ").split(",")], [float(x) for x in input("Enter the frequency for each x-Value: ").split(",")]


#logic to find mean 
    mean = sum(x*f for x, f in zip(X, f))/sum(f)
    print ("Mean is " + str(mean) )


#logic to find mean deviation 
    meanDeviation = [x - mean for x in X]
    print ("The Mean Devaitions are: ", str(meanDeviation))


#logic to find squares of the Mean Deviation 
    absoluteMeanDeviation= [x**2 for x in meanDeviation]
    print ("The square of Mean Deviations are: ", str(absoluteMeanDeviation))


#logic to check if user wants to find sample or population standard deviation and variance 
    popuSamp = input ("Do you want to calculate Popoulation Variance (P) or Sample Variance(S). P/S \n")


#logic for population standard deviation and variance 
    if (popuSamp == "P" or popuSamp == "p"):
        variance = sum(absoluteMeanDeviation)/sum(f)
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)


#logic for sample standard deviation and variance 
    elif (popuSamp == "S" or popuSamp == "s"):
        variance = sum(absoluteMeanDeviation)/(sum(f) - 1)
        print ("The variance is: ", float(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", float(standardDeviation))


#logic for ungrouped data sets 
elif (dataType == "N" or dataType == "n"):
    X = [float(x) for x in input("Enter your x-Values: ").split(",")]


#logic to find number of elements in set 
    count = len(X)


#logic to find mean 
    mean = sum(X)/count
    print ("Mean is ", + mean)


#logic to find mean deviation 
    meanDeviaton = [x - mean for x in X]


#logic to find square of mean deviations
    absoluteSquareMeanDeviation = [x**2 for x in meanDeviaton]


#logic for population or sample variance and standard 
    popuSamp = input ("Do you want to calculate Popoulation Variance (P) or Sample Variance(S). P/S \n")


#logic for population variance and standard deviation 
    if (popuSamp == "P" or popuSamp == "p"):
        variance = sum(absoluteSquareMeanDeviation)/count
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)


#logic for sample variance and standard deviation 
    elif (popuSamp == "S" or popuSamp == "s"):
        variance = sum(absoluteSquareMeanDeviation)/(count - 1)
        print ("The variance is: ", str(variance))
        standardDeviation = sqrt(variance)
        print ("The Standard Deviation is: ", + standardDeviation)
