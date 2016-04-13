class Heap():
    
    def __init__(self, alist):
        self.array = alist
        self.len_array = len(alist)

    def __parent(self, i):
        return (i-1)//2
        
    def __left(self, i):
        return 2*i+1
        
    def __right(self, i):
        return 2*i+2
        
    def __changeElem(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
    def maxHeapify(self, i):
        l = self.__left(i)
        r = self.__right(i)
        if l <= self.len_array-1 and self.array[l] > self.array[i]:
            maior = l
        else:
            maior = i
        if r <= self.len_array-1 and self.array[r] > self.array[maior]:
            maior = r
        if maior != i:
            self.__changeElem(i, maior)
            self.maxHeapify(maior)
            
    def build_maxHeapify(self):
        for i in range(self.len_array-1//2,-1,-1):
            self.maxHeapify(i)
            
    def heapsort(self):
        self.build_maxHeapify()
        for i in range(self.len_array-1,0,-1):
            self.__changeElem(0,i)
            self.len_array -= 1
            self.maxHeapify(0)
            
l=[5,3,2,7,1,9,8]
x = Heap(l)
x.heapsort()
print(x.array)