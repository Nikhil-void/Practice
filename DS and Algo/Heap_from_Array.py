# python3

def get_p(data, i):
    if i > 0:
        return(data[(i-1) / 2])
    else: return data[i]

def get_l_r_c(data, i):
    l = (2*i)+1
    r = (2*i)+2
    lc = rc = -1
    if len(data) > l:
        lc = data[l]
        #l = -1
    if len(data) > r:
        rc = data[r]
        #r = -1
    return (l, lc, r, rc)


def shift_up(data, i, shifts):
    #i = 1
    #cur=4
    cur = data[i]
    curMax = i
    li, lc, r, rc = get_l_r_c(data, i)
    #print(li, lc, r, rc, i, curMax, "--")
    if (lc != -1) and (lc < cur):
        curMax = li
    #print(li, lc, r, rc, i, curMax)
    if rc != -1 and rc < data[curMax]:
        curMax = r
    if i != curMax:
        temp = data[i]
        data[i] = data[curMax]
        data[curMax] = temp
        shifts.append((i,curMax))
        shift_up(data, curMax, shifts)
    

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    shifts = []
    for i in range(int(len(data)/2), -1, -1):
        #print("i = ", i)
        shift_up(data, i, shifts)
    return shifts


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
