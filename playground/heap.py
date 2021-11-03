
def swap(array, i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


class Heap:
    def __init__(self, length):
        self.n = 0
        self.array = [None] * length    


    def insert(self, x):
        self.array[self.n] = x
        self.n +=1

        i = self.n -1
        while i > 0 and self.array[i] < self.array[(i-1)//2]:
            swap(self.array, i, (i-1)//2)
            i = (i-1) // 2 

    def remove_min(self):
        swap(self.array, 0, self.n-1)
        self.n -=1
        root = 0
        left = (2*root) + 1 
        right = left + 1
        current = left
        while current < self.n:
            right_val = self.array[right]
            left_val = self.array[left]
            if right < self.n and right_val  < left_val: 
                current = right
            if self.array[current] >= self.array[root]:
                break
            swap(self.array, root, current)
            root = current
            left = (2*current) + 1
            current = left
            right = left + 1
        return self.array[self.n] 

    def sort(self, array):
        for item in array:
            self.insert(item)
        i = 0 
        while i < len(array):
            array[i] = self.remove_min()
            i +=1

a = [23, 34, 12, 100, 3, 30, 200, 4]
b = a[:] 
b.sort()

h = Heap(len(a))
h.sort(a)
assert a == b
