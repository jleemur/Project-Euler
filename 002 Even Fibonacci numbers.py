# Jonathan Murray
# Project Euler
# Problem 2: Even Fibonacci numbers

# Recursive method to count all even fibonacci values under 4,000,000
def evenFibonacciSum(prev, curr, sum):
    if curr%2==0:
        sum += curr
    if prev+curr > 4000000:
        return sum
    return evenFibonacciSum(curr, prev+curr, sum)

if __name__ == "__main__":
    print(evenFibonacciSum(1,2,0))
