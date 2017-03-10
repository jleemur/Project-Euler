# Returns the 10 left-most digits of the sum of n_arr
def get_large_sum(n_arr):
    sum = 0L
    # go through loop and add numbers together... so innovative
    for i in n_arr:
        sum += i
    return str(sum)[:10]

if __name__ == "__main__":
    n_arr = []

    # 100 50-digit numbers
    f = open('013_Large_sum.txt', 'r')
    for line in f:
        n_arr.append(int(line))

    print(get_large_sum(n_arr))
