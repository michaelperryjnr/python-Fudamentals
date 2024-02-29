#create an empty array for  prime numbers
primeNumsStart = int(input("Enter the start of your prime numbers range \n"))
primeNumsEnd = int(input("Enter the end of your prime numbers range \n"))


primeNumbers = []
#code to generate numbers from 2 to 98
for x in range(primeNumsStart,primeNumsEnd):
    #this code checks if the number is actually a primenumber
    for n in range(2,x):
        if x % n == 0:
            break
    else:
        primeNumbers.append(x)
#the prime numbers are printed and summed with the code below
primeNumbers.remove(2)
print(primeNumbers)
numberOfPrimes = f"The number of prime numbers between {primeNumsStart} and {primeNumsEnd} is {len(primeNumbers)}"
print(numberOfPrimes)
print("The sum of Prime Numbers are", sum(primeNumbers))
