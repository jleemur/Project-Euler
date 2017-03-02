# Returns the sum of all primes up to :n:
def sum_primes(n):
    nums = list(range(2,n)) #create list from 2 to :n:

    #check if number i is prime, if it is: make all multiples of i negative
    #sieve of eratos
    for i in range (0, int(len(nums)**0.5)+1):
        if nums[i] > 0 and is_prime(nums[i]):
            for j in range (i+nums[i], len(nums), nums[i]):
                if nums[j] > 0:
                    nums[j] *= -1

    #sum all positive numbers
    sum = 0
    for i in range(0,len(nums)):
        if nums[i] > 0:
            sum += nums[i]

    return sum

#copied method from 003
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(sum_primes(2000000))
