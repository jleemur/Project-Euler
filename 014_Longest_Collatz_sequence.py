## if n==even: n/2, if n==odd: 3n+1... stop when n==1
def find_longest_collatz_sequence(n):
    dict = {1: 1} #{value: collatz sequence from value}
    max_chain = 1

    # Check all values from 2 to n
    for val in range(2, n):
        chain_length = 0
        found = False
        curr = val

        while not found:
            if curr in dict:
                #add current chain length to chain length found in :dict:
                dict[val] = dict[curr] + chain_length
                found = True
                if (dict[val] > dict[max_chain]):
                    max_chain = val
            elif curr % 2 == 0:
                chain_length += 1
                curr = curr / 2
            else:
                chain_length += 1
                curr = 3 * curr + 1

    return max_chain



if __name__ == "__main__":
    print(find_longest_collatz_sequence(1000000))
