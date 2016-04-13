def bubble_sort(alist):
    for num in range(len(alist)-1, 0, -1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist
    
l=[5,3,2,7,1,9,8]
x = bubble_sort(l)
print(x)
