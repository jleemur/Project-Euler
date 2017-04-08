from operator import mul
from fractions import Fraction

def get_combinatoric_selections(n):
    result = 0

    for i in range(1, n+1):
        for j in range(1, i+1):
            if nCr(i, j) > 1000000:
                result += 1

    return result


def nCr(n, r):
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(r)), 1) )

if __name__ == "__main__":
    print(get_combinatoric_selections(100))
