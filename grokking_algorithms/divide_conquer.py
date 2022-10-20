


def dc(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[-1] + dc(array[:-1])
array = [1,2,3,10]
res = dc(array)
print(res)


def maximum(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    maxy = maximum(array[:-1])
    return maxy if maxy > array[-1] else array[-1]


def binary_search(array, item, low, high):
    mid = low + (high - low) // 2
    if len(array) == 1:
        return array[0] if array[0] == item else None
    return binary_search(array[mid+1:], item, low, mid) if item > array[mid] else binary_search(array[:mid-1], item, mid, high)

s = binary_search(array, 4, 0, len(array)-1)
print(s)
