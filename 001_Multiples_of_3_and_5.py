# Count multiples of :mult1: and :mult2: from 3 to :range:
def sumMultiples(mult1, mult2, upLimit):
    sum = 0
    # O(n) - I could improve this by incrementing i by: 3,2,1,3,1... Not sure how to get this quicker than linear time...
    for i in range(min(mult1, mult2), upLimit):
        if i%mult1==0 or i%mult2==0:
            sum += i
    return sum

if __name__ == "__main__":
    print(sumMultiples(3, 5, 1000)) #all multiples of 3 & 5 BELOW 1000
