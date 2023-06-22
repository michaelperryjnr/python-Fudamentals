primeNumbers = []
for x in range(2,98):
    for n in range(2,x):
        if x % n == 0:
            break
    else:
        primeNumbers.append(x)
print(primeNumbers)
print("The sum of Prime Numbers are", sum(primeNumbers))
