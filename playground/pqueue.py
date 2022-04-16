



class Queue():

    def __init__(self, D = 2):
        self.D = D
        self.pairs = []
        self.map = {} 

    def get_parent_index(self, index):
        return (index-1) // self.D

    def first_leaf_index(self):
        return len(self.pairs) // self.D
        return ((len(self.pairs) - 2) // (self.D+1))

    def swap(self, index1, index2):
        temp = self.pairs[index1]
        self.pairs[index1] = self.pairs[index2]
        self.pairs[index2] = temp
        el1 = self.pairs[index1]['element']
        el2 = self.pairs[index2]['element']
        self.map[el1] = index1
        self.map[el2] = index2
        print(self.map)
        print(self.pairs)

    def highest_priority_child(self, index):
        child = None
        highest_index = -1
        for i in range(1, self.D+1):
            highest_index = (2 * index) + i
            if highest_index >= len(self.pairs):
                highest_index = -1
                break
            if i == 1:
                child = self.pairs[highest_index]
            elif self.pairs[highest_index]['priority'] > child['priority']:
                child = self.pairs[highest_index]
        return child, highest_index

    def peek(self):
        return self.pairs[0]['element']

    def top(self):
        if len(self.pairs) == 0:
            return None
        p = self.pairs.pop()
        if len(self.pairs) == 0:
            return p['element']
        else:
            target = self.pairs[0]
            self.pairs[0] = p
            self.push_down(0)
            return target['element']

    def insert(self, e, p):
        p = {'element': e, 'priority': p}
        self.pairs.append(p)
        self.map[e] = len(self.pairs)-1
        self.bubble_up(len(self.pairs)-1)

    def update(self, old_value, new_priority):
        index = self.find(old_value)
        print('here is the index')
        print(index)
        if index >= 0:
            old_priority = self.pairs[index]['priority']
            self.pairs[index] = {'element': old_value, 'priority': new_priority}
            if new_priority < old_priority: 
                print('time to push down')
                self.push_down(index)
            else:
                self.bubble_up(index)

    def remove(e):
        return None

    def find(self, el):
        if el in self.map:
            return self.map[el]
        return None

    def push_down(self, index):
        current_index = index
        print(current_index, self.first_leaf_index())
        while current_index < self.first_leaf_index():
            print('whiling')
            child, child_index = self.highest_priority_child(current_index)
            if child['priority'] > self.pairs[current_index]['priority']:
                self.swap(current_index, child_index)
                current_index = child_index
            else:
                break
    def bubble_up(self, index):
        parent_index = index
        while parent_index > 0:
            current_index = parent_index
            parent_index = self.get_parent_index(parent_index)
            if self.pairs[parent_index]['priority'] < self.pairs[current_index]['priority']:
                self.swap(current_index, parent_index)
            else:
                break


def main():
    q = Queue(3)
    q.insert('low', 3)
    q.insert('medium', 12)
    q.insert('lowest', 2)
    q.insert('high', 14)
    q.update('high', 1)
    print('top')
    print(q.peek())
    print(q.top())
    print(q.top())
    print(q.top())
    


if __name__ == "__main__":
    main()
