def merge(array, ):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and array[j - 1] > key:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key

array = [5,3,2,7,1,9,8]
array_sort = insertion_sort(array)
print(array_sort)