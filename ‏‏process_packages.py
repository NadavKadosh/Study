import numpy
class queue:
    def __init__(self, max_size = 10**5):
        self.max_size = max_size-1
        self.items = []
    def isempty(self):
        return self.items == []
    def enqueue(self,item):
        if len(self.items) < self.max_size+1:
            self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)
    def get_max_size(self):
        return self.max_size
    def get(self):
        return self.items
    def first(self):
        if len(self.items) == 0:
            return []
        else:
            return self.items[len(self.items)-1]

def process(S, processes):
    if processes == []:
        return []
    to_do = queue(S)
    max_time= max(max([i[0]+i[1] for i in processes]), 1) + 1
    first_in_queue = 0
    for time in range(max_time):
        if first_in_queue < len(processes):
            while processes[first_in_queue][0] == time:
                to_do.enqueue(processes[first_in_queue])
                if to_do.first()[1] == 0:
                    to_do.first()[2] = time
                    to_do.dequeue()
                first_in_queue += 1
                if first_in_queue == len(processes):
                    break
        if to_do.size() != 0:
            if to_do.first()[0] <= time:
                to_do.first()[2] = time
            if to_do.first()[1] < time:
                continue
            if to_do.first()[1] == time + 1 or to_do.first()[0] == to_do.first()[1]:
                to_do.dequeue()
          
    return processes

data1 = [int(i) for i in input().split()]
S = data1[0]
n = data1[1]
processes = []
for i in range(n):
    item = [int(i) for i in input().split()]
    item.append(-1)
    processes.append(item)

after_process = process(S, processes)
for i in after_process:
    print(i[2])
