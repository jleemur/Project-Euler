# Returns the largest prime factor of :n:
def largest_prime_factor(n):
    primes = [] #possible results
    factors = [] #factors of n, and their factors, and...

    # add all factors of n
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)

    #for all possible factors, check
    for val in factors:
        if (not (val in primes)) and (is_prime(val)):
            primes.append(val)
        else:
            #add all factors of val - which apparently extends the for loop *success*
            for i in range(2, int(val**0.5)+1):
                if val % i == 0:
                    if not (i in factors):
                        factors.append(i)
                        factors.append(val/i)

    primes.sort(reverse=True)
    return primes[0]

#TODO: make this more efficient for fun :)
def is_prime(n):
    #no possible factors after sqrt(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(largest_prime_factor(600851475142))
