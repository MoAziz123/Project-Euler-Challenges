num = 30
#get the factors even if it's computationally expensive...
#for large sets at least
def getFactors(num):
    factors = []
    for i in range(num+1):
        for x in range(num+1):
            if x * i == num:
                factors.append(x)
    print("Factors completed!")
    return factors

#reduce into prime factors
def getPrimeFactors(list):
    primes = []
    for i in list:
        list = []
        list.extend(getFactors(i))
        if len(list) == 2: #because the prime factors have a list count of 2 it should be appended to primes
            primes.append(i)
    print("Primes completed!")
    return primes

def getLargestPrimeFactor(list):
    highest = list[0]
    for i in list:
        if i > highest:
            highest = i
    print("Highest total completed!")
    return highest

print(getLargestPrimeFactor(getPrimeFactors(getFactors(int(input("Enter a number: "))))))
    
