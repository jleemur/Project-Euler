from operator import mul
from fractions import Fraction

###
# Method 1: combinatorics
def get_lattice_paths_1(n, m):
  return nCr(n+m, n)

def nCr(n, r):
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(r)), 1) )


###
# Method 2: dynamic programming
def get_lattice_paths_2(n, m):
    sum = n+m #add 1's from base path
    matrix = [[0]*m for i in range(n)]

    #base path 1..n by 1..m
    for i in range(0, n):
        matrix[i][0] = 1
    for i in range(0, m):
        matrix[0][i] = 1

    for down in range(1, n):
        for right in range(1, m):
            # matrix[up][] + matrix[][left]
            up_left_sum = matrix[down-1][right] + matrix[down][right-1]

            #update matrix, update sum
            matrix[down][right] = up_left_sum
            sum += matrix[down][right]

    return sum


###
# Method 3: recursion x_x
def get_lattice_paths_3(n, m):
    return recur_lattice_paths(n, m, 0, 0, 0)

def recur_lattice_paths(n, m, down, right, sum):
    if right == m and down == n:
        return 1
    elif down > n or right > m:
        return 0
    return recur_lattice_paths(n, m, down+1, right, sum) + recur_lattice_paths(n, m, down, right+1, sum)


if __name__ == "__main__":
    # n, m grid
    print(get_lattice_paths_1(20, 20))
    print(get_lattice_paths_2(20, 20))
    #print(get_lattice_paths_3(20, 20))
