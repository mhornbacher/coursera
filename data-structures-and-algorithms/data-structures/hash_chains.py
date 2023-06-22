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
        # MY elems list:
        self.hash_table = [[] for i in range(self.bucket_count)]

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

    # def process_query(self, query):
    #     if query.type == "check":
    #         # use reverse order, because we append strings to the end
    #         self.write_chain(cur for cur in reversed(self.elems)
    #                     if self._hash_func(cur) == query.ind)
    #     else:
    #         try:
    #             ind = self.elems.index(query.s)
    #         except ValueError:
    #             ind = -1
    #         if query.type == 'find':
    #             self.write_search_result(ind != -1)
    #         elif query.type == 'add':
    #             if ind == -1:
    #                 self.elems.append(query.s)
    #         else:
    #             if ind != -1:
    #                 self.elems.pop(ind)

    # MY CODE STARTS HERE
    def process_query(self, query):
        if query.type == 'check':
            self.write_chain(cur for cur in reversed(self.hash_table[query.ind]))
        else: # we need to compute the hash regardless of what other command is sent
            cur_hash = self._hash_func(query.s) # compute the hash of the item
            # get the index if the item exists in the hash table
            try:
                ind = self.hash_table[cur_hash].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'add':
                if ind == -1:
                    self.hash_table[cur_hash].append(query.s)
            elif query.type == 'del':
                if ind != -1:
                    self.hash_table[cur_hash].pop(ind)
            elif query.type == 'find':
                self.write_search_result(ind != -1)


    # MY CODE ENDS HERE

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
