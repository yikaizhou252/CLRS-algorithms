from util import test_sort
import big
name = "heap sort"

class Heap(list):
    def __init__(self, lst: list):
        self.extend(lst) # add argument list to initial list
        self.heap_size = 0

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1) # diff than book because index starts at 0
    
    def parent(self, i):
        if i == 0: raise IndexError("Root node does not have parents")
        return int((i + 1)/2) - 1

    def build_max_heap(self):

        self.heap_size = len(self)
        if self.heap_size == 1: return # already a max heap

        # boundary + 1 is the first leaf node
        boundary = int(len(self)/2) - 1

        for i in range(boundary, -1, -1):
            self.max_heapify(i)

    def sort(self):
        for i in range(len(self)):
            # temp = self[self.heap_size - 1]
            # self[self.heap_size - 1] = self[0]
            # self[0] = temp
            self.swap(0, self.heap_size - 1)
            self.heap_size -= 1
            self.max_heapify(0)

    def swap(self, i, j):
        if i < len(self) and j < len(self):
            temp = self[i]
            self[i] = self[j]
            self[j] = temp
        else: raise IndexError(f'Swapping index out of range\n i: {i}, j: {j}, len(heap): {len(self)}')


    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = 0

        if l <= self.heap_size - 1 and self[l] > self[i]:
            largest = l

        else: largest = i

        if r <= self.heap_size - 1 and self[r] > self[largest]:
            largest = r


        if largest != i:

            # exchange

            self.swap(i, largest)
            # temp = self[i]
            # self[i] = self[largest] 
            # self[largest] = temp
            # exchange

            self.max_heapify(largest)

        

    def min_heapify(self):
        return



def heap_sort(lst: list):
    h = Heap(lst)
    h.build_max_heap()
    h.sort()
    return h

# h = Heap([1,2,3,6,5])
# h.build_max_heap()
# print(h)
test_sort(heap_sort, name)
# heap_sort([10,20,25,6,12,15,4,16])