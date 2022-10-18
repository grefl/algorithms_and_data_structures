

numbers = [1,2,40, 200, 4]

def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        print(mid)
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None 


if __name__ == "__main__":
    res = binary_search(numbers, 1)
    print(res)

