import numpy

def merge(array, p, q, r):
    x = q - p + 1
    y = r - q
    left = [None] * x
    right = [None] * y
    for i in range(x):
        left[i] = array[p + i - 1]
    for j in range(y):
        right[j] = array[q + j]
    left.append(numpy.inf)
    right.append(numpy.inf)
    i = 0
    j = 0
    for k in range(p - 1, r):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
             
def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)
 
array = [5, 3, 1, 2, 6, 4]
merge_sort(array, 0, len(array))
print(array)