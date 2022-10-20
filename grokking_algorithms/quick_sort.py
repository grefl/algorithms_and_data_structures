
def qsort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    lesser  = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    print(lesser, greater)
    left = qsort(lesser)
    left.append(pivot)
    left += qsort(greater)
    return left


array = [13,1, 100, 2, 10213, 1231, 123, 7]

print(qsort(array))
