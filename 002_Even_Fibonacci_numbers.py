# Recursive method to count all even fibonacci values below :upperLimit:
def get_even_fibonacci_sum(prev, curr, sum, upperLimit):
    if curr%2==0:
        sum += curr
    if prev+curr > upperLimit:
        return sum
    return get_even_fibonacci_sum(curr, prev+curr, sum, upperLimit)

if __name__ == "__main__":
    print(get_even_fibonacci_sum(1,2,0,4000000))
