
def swap(array, i, j):
    temp     = array[i]
    array[i] = array[j]
    array[j] = temp
    

class Queue:
    def __init__(self, length):
        self.pairs = [None] * length
        self.n = 0

    def bubble_up(self, index):
        parent_index = index 

        while parent_index > 0:
            current_index = parent_index
            print(self.pairs)
            parent_index = (parent_index - 1) // 2
            print(parent_index, current_index)
            if (parent_index > 0 and current_index > 0) and (self.pairs[parent_index] not None and self.pairs[current_index] not None) and self.pairs[parent_index]['priority'] < self.pairs[current_index]['priority']:
                swap(self.pairs, current_index, parent_index)
            else:
                break
    def top(self):
        return self.pairs[0]
    def peek(self):
        pass
    def insert(self, description, priority):
        self.pairs[self.n] = {'description': description, 'priority': priority}
        self.n +=1
        self.bubble_up(self.n)


s = Queue(10)
s.insert('hi', 3)
s.insert('low', 1)
s.insert('medium', 2)
print(s.top())
