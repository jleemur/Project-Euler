# Recursive method to count all even fibonacci values below :upLimit:
def getEvenFibonacciSum(prev, curr, sum, upLimit):
    if curr%2==0:
        sum += curr
    if prev+curr > upLimit:
        return sum
    return getEvenFibonacciSum(curr, prev+curr, sum, upLimit)

if __name__ == "__main__":
    print(getEvenFibonacciSum(1,2,0,4000000))
