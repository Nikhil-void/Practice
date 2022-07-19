# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


def hash_func(s, bucket_count):
    multiplier = 263
    prime = 1000000007
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans % bucket_count

def process():
    bucket_count = int(input())
    n = int(input())
    d1 = {i:[] for i in range(bucket_count)}
    for i in range(n):
        task, val = input().split(' ')
        #h = -1
        if task in ["add", "find", "del"]:
            h = hash_func(val, bucket_count)
        else:
            h = int(val)
        if task == "add":
            if not val in d1[h]:
                d1[h].insert(0, val)
        elif task == "find":
            #print(val, h, d1)
            if val in d1[h]:
                print("yes")
            else:
                print("no")
        elif task == "del":
            if val in d1[h]:
                d1[h].remove(val)
        elif task == "check":
            if len(d1[h]) == 0:
                print()
            else:
                for i in d1[h]:
                    print(i, end=' ')
                print()
        #print(task, d1)
    
if __name__ == '__main__':
    process()
 
