# Selection sort
def findsmallesr(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallesr(arr)
        newArr.append(arr.pop(smallest))
    return newArr

list = [99999, 54545, 8, 77, 43, 0, 1, 23, 11, 87, 134]
print(selectionsort(list))