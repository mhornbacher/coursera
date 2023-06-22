# python3

# MY CODE STARTS HERE
import math
class ThreadMinHeap:
    def __init__(self):
        self.array = []

    def append(self, thread):
        self.array.append(thread)

    def getMin(self):
        return self.array[0]
    # Get the related objects
    def Parent(self, i):
        return math.ceil(i/2) - 1
    def LeftChild(self, i):
        return (2 * i) + 1
    def RightChild(self, i):
        return (2 * i) + 2
    # Move the item untill both its children are less then it
    def SiftDown(self, i):
        minIndex = i
        l = self.LeftChild(i)
        if l < len(self.array):
            if self.array[l][1] < self.array[minIndex][1] or (self.array[l][1] == self.array[minIndex][1] and self.array[l][0] < self.array[minIndex][0]):
                minIndex = l
        r = self.RightChild(i)
        if r < len(self.array):
            if self.array[r][1] < self.array[minIndex][1] or (self.array[r][1] == self.array[minIndex][1] and self.array[r][0] < self.array[minIndex][0]):
                minIndex = r
        if i != minIndex:
            self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
            self.SiftDown(minIndex) # Call siftDown again until i==minIndex

    # Build the Min-Heap
    def BuildHeap(self):
        n = len(self._data)
        for i in range(math.ceil(n/2) + 1, -1, -1):
            self.SiftDown(i)


    def updateMin(self, new_value):
        self.array[0][1] = new_value
        self.SiftDown(0)
# MY CODE ENDS HERE

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.log = [] # I added this to keep track of output
        assert m == len(self.jobs)

    def write_response_old(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs_slow(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
                self.assigned_workers[i] = next_worker
                self.start_times[i] = next_free_time[next_worker]
                next_free_time[next_worker] += self.jobs[i]

    # MY CODE STARTS HERE
    def assign_jobs(self):
        # O(m) operation as it creates the array
        self.threads = ThreadMinHeap()
        for i in range(0, self.num_workers):
            self.threads.append([i, 0])
        jobs_left = 0
        for job in self.jobs:
            thread = self.threads.getMin()
            self.log.append((thread[0], thread[1]))
            new_value = thread[1] + job
            self.threads.updateMin(new_value)
            jobs_left += 1

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.log[i][0], self.log[i][1]) 

    # MY CODE ENDS HERE

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

