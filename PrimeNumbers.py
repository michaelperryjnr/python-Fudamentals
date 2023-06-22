#create an empty array for  prime numbers
primeNumbers = []
#code to generate numbers from 2 to 98
for x in range(2,98):
    #this code checks if the number is actually a primenumber
    for n in range(2,x):
        if x % n == 0:
            break
    else:
        primeNumbers.append(x)
#the prime numbers are printed and summed with the code below
print(primeNumbers)
print("The sum of Prime Numbers are", sum(primeNumbers))
