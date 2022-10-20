# Arrays and Linked Lists


## Arrays

Arrays are great if you want to statically allocate memory and not grow this data structure. This is because an array needs to know how many items will be used since they are allocated together into memory together. So you can index from one item to the next without jumping around to far flung address elsewhere in your memory space.


## Linked Lists

Linked Lists can grow and shrink without needing any preallocation. This makes them very good for inserts. You don't need the memory to be allocated in the same place because each element that is inserted has a link to the next element. But the issue for this is that if you want to get to the last element, you will need to traverse the entire list. Which means look up/search is O(n)
