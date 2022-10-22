def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

list = [99999, 54545, 8, 77, 43, 0, 1, 23, 11, 87, 134]
print(quicksort(list))