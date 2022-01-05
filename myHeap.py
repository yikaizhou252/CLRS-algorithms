class Heap(list):
    def __init__(self, lst: list):
        self.extend(lst) # add argument list to initial list
        self.length = len(self) # this changes dynamically

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2 # diff than book because index starts at 0

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = 0

        if l <= self.length - 1 and self[l] > self[i]:
            largest = l

        else: largest = i

        if r <= self.length - 1 and self[r] > self[i]:
            largest = r


        if largest != i:

            # exchange
            temp = self[i]
            self[i] = self[largest] 
            self[largest] = temp
            # exchange
            
            self.max_heapify(largest)

        

    def min_heapify(self):
        return


h = Heap([10,20,25,6,12,15,4,16])
h.max_heapify(3)
h.max_heapify(2)
h.max_heapify(0)
h.max_heapify(2)
h.max_heapify(0)


print(h)