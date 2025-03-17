class Stack:
    def __init__(self):
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.is_empty() is False:
            return self.storage.pop()
        return 'Empty Stack'

    def peek(self):
        if self.is_empty() is False:
            return self.storage[-1]
        return 'Empty Stack'

    def display(self):
        if self.is_empty() is False:
            storage_copy = self.storage.copy()
            while self.is_empty() is False:
                print(self.peek())
                self.pop()
            self.storage = storage_copy

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

stack.display()
print(stack.is_empty())



class Queue:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.count = 0
        self.capacity = capacity

    def is_full(self):
        return self.count == self.capacity - 1

    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        if self.is_full() is False:
            self.storage[self.count] = value
            self.count += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if self.is_empty() is False:
            item = self.storage[0]
            for i in range(1, self.count):
                self.storage[i-1] = self.storage[i]
            self.storage[self.count] = None
            self.count -= 1
        return 'Queue is empty'

    def display(self):
        if self.is_empty() is False:
            for i in range(self.count):
                print(self.storage[i], end=' ')
            return
        return 'Queue is empty'

queue = Queue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()

queue.display()


print('\nLinked List')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head

        while temp.next:
            print(temp.value, end=' -> ')
            temp = temp.next
        print(temp.value)


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(4)
linked_list.append(3)
linked_list.append(10)

linked_list.display()












