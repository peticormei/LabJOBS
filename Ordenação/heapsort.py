class Heap():
    
    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)

    def parent(self, i):
        return (i-1) // 2
        
    def left(self, i):
        return (2 * i) + 1
        
    def right(self, i):
        return (2 * i) + 2
        
    def exchange(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left <= (self.heap_size - 1) and self.array[left] > self.array[i]:
            maior = left
        else:
            maior = i
        if right <= (self.heap_size - 1) and self.array[right] > self.array[maior]:
            maior = right
        if maior != i:
            self.exchange(i, maior)
            self.max_heapify(maior)
            
    def build_max_heap(self):
        for i in range((self.heap_size // 2), -1, -1):
            self.max_heapify(i)
            
    def heapsort(self):
        self.build_max_heap()
        for i in range((self.heap_size - 1), -1, -1):
            self.exchange(0,i)
            self.heap_size -= 1
            self.max_heapify(0)
            
array = [5, 3, 1, 2, 6, 4]
heap = Heap(array)
heap.heapsort()
print(heap.array)