# Recursive method to count all even fibonacci values below :upperLimit:
def getEvenFibonacciSum(prev, curr, sum, upperLimit):
    if curr%2==0:
        sum += curr
    if prev+curr > upperLimit:
        return sum
    return getEvenFibonacciSum(curr, prev+curr, sum, upperLimit)

if __name__ == "__main__":
    print(getEvenFibonacciSum(1,2,0,4000000))
