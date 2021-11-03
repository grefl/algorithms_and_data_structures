



def bubble_sort(array):
    i = 0
    j = i
    while i < len(array):
        j = i
        while j < len(array):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            j+=1        
        i +=1

a = [12, 200, 1, 3000, 30023, 123, 12]
bubble_sort(a)
print(a)

