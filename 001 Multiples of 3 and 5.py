# Jonathan Murray
# Project Euler
# Problem 1: Multiples of 3 and 5

# Count multiples of 3 and 5 from: 3 to range
def getSum(max):
    sum = 0
    # O(n) - I could improve this by incrementing i by: 3,2,1,3,1... Not sure how to get this quicker than linear time...
    for i in range(3,max):
        if i%3==0 or i%5==0:
            sum += i
    return sum

if __name__ == "__main__":
    print(getSum(1000)) #all multiples BELOW 1000
