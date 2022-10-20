


def find_smallest(array):
    smallest = [0,array[0]]
    for index in range(1, len(array)):
        if array[index] < smallest[1]:
            print(array[index])
            smallest[1] = array[index] 
            smallest[0] = index
    return smallest[0]



def selection_sort(array):
    sorted_array = []
    while len(array):
        smallest_index = find_smallest(array) 
        sorted_array.append(array.pop(smallest_index))
    return sorted_array



sorted_array = selection_sort([12, 1, 3, 20])
print(sorted_array)

