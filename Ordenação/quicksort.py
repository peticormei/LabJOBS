'''
Created on 14 de abr de 2016

@author: Aluno
'''
def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q+1, r)
        
l = [2,5,6,1,2,3,7,8]
quicksort(l, 0, len(l)-1)
print(l)