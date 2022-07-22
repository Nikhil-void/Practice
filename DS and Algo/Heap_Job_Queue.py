# python3

from collections import namedtuple

#AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def get_p(data, i):
    if i > 0:
        return(data[(i-1) / 2])
    else: return data[i]

def get_l_r_c(data, i):
    l = (2*i)+1
    r = (2*i)+2
    lc = rc = (-1, -1)
    if len(data) > l:
        lc = data[l]
        #l = -1
    if len(data) > r:
        rc = data[r]
        #r = -1
    return (l, lc, r, rc)


def shift_up(data, i):
    #i = 1
    #cur=4
    cur = data[i][0]
    curMax = i
    li, lc, r, rc = get_l_r_c(data, i)
    #print(li, lc, r, rc, i, curMax, "--")
    if (lc[0] != -1) and (lc[0] < cur):
        curMax = li
    if (lc[0] != -1) and lc[0] == cur and lc[1] < data[i][1]:
        curMax = li
    #print(li, lc, r, rc, i, curMax)
    if rc[0] != -1 and rc[0] < data[curMax][0]:
        curMax = r
    if rc[0] != -1 and rc[0] == data[curMax][0] and rc[1] < data[curMax][1]:
        curMax = r
    if i != curMax:
        temp = data[i]
        data[i] = data[curMax]
        data[curMax] = temp
        #shifts.append((i,curMax))
        shift_up(data, curMax)

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
    #shifts = []
    for i in range(int(len(data)/2), -1, -1):
        #print("i = ", i)
        shift_up(data, i)
    return None

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    #result = []
    next_free_time = [[0, i] for i in range(n_workers)]
    count = 0
    for job in jobs:
        #next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        if count <n_workers:
            next_worker = next_free_time[count][1]
            #result.append(AssignedJob(next_worker, next_free_time[next_worker]))
            print(next_worker, next_free_time[next_worker][0])
            next_free_time[next_worker][0] += job
        if count >= n_workers:
            #for i in 
            next_time, next_worker = next_free_time[0]
            print(next_worker, next_time)
            next_free_time[0] = (next_time+job, next_worker)
            shift_up(next_free_time, 0)
        count += 1
        if count == n_workers:
            build_heap(next_free_time)
    return None


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    assign_jobs(n_workers, jobs)

    #for job in assigned_jobs:
    #    print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
    """
    a = [(6,'a'), (4,'b'),(5,'c'),(1,'d'),(2,'e'),(3,'f')]
    shift_up(a,0)
    print(a)
    next_free_time = [(0, i) for i in range(10)]
    print(next_free_time)
    """
