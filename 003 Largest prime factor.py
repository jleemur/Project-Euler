# Jonathan Murray
# Project Euler
# Problem 3: Largest prime factor
def largestPrimeFactor(n):
    primes = []
    factors = []

    #no possible factors > sqrt(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)

    for val in factors:
        print val
        if (not val in primes) and isPrime(val):
            primes.append(val)
        else:
            for i in range(2, int(val**0.5)+1):
                if val % i == 0:
                    if (not i) in factors:
                        factors.append(i)
                        factors.append(val/i)
    print primes
    primes.sort()
    return primes[len(primes)-1]

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    #print(solve(13195))
    print(largestPrimeFactor(600851475142))
