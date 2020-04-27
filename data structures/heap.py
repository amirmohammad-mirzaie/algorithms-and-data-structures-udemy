class Heap(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_size = 0
        self.heap = [0] * self.capacity

    def insert(self, item): # insertion
        if self.capacity == self.heap_size:
            print('heap if full, %s cannot be stored' % item)
            return
        self.heap[self.heap_size] = item
        self.heap_size += 1

        self.fix_up(self.heap_size-1)

    def fix_up(self, index): # move an item from bottom to the root and swap values if necessary
        parent_index = (index-1)//2

        if index>0 and self.heap[index]>self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2): # method for swapping two values
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_max(self): # getting the first element of the array (assuming it is sorted)
        return self.heap[0]

    # getting the first element of sorted array and moving it
    # to the end of the array and decrease the size of the heap
    def poll(self):
        max = self.get_max()
        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size - 1
        self.fix_down(0)

        return max
    # fixing violations from a node to the bottom (leaves)
    def fix_down(self, index):
        index_left = 2*index+1
        index_right = 2*index+2

        index_largest = index

        if index_left<self.heap_size and self.heap[index_left]>self.heap[index]:
            index_largest = index_left

        if index_right<self.heap_size and self.heap[index_right]>self.heap[index_largest]:
            index_largest = index_largest

        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)

    # using a combination of above defined methods to sort using heaps
    def heap_sort(self):
        size = self.heap_size

        for i in range(size):
            max = self.poll()
            print(max)

# testing the heap
if __name__ == '__main__':
    heap = Heap(capacity=10)
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(318)
    heap.insert(319)
    heap.insert(320)
    heap.insert(321)
    heap.insert(322)
    heap.insert(323)
    heap.heap_sort()

#%%
# using the heap library in python
from heapq import heapify, heappop, heappush

heap = []
nums = [12,3,-5,0,3,6,80]

for num in nums:
    heappush(heap, num)
while heap:
    print(heappop(heap))
heapify(nums)
print(nums)
