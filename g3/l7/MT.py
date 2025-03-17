



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # 20





class Queue:
    def __init__(self, size=100):
        self.queue = [None] * size
        self.front = 0
        self.back = 0
        self.size = size
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            print("The queue is full!")
            return
        self.queue[self.back] = value
        self.back = (self.back + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty!")
            return None
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def front_value(self):
        return None if self.is_empty() else self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size


queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())  # 10
print(queue.front_value())  # 20




class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3 -> None




def is_valid_parentheses(s):
    st = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            st.push(char)
        elif char in ")]}" and (not st or st.pop() != pairs[char]):
            return False
    return not st

print(is_valid_parentheses("(())"))  # True
print(is_valid_parentheses("({[)]}"))  # False




queue = Queue()
queue.enqueue("Task 1")
queue.enqueue("Task 2")
queue.enqueue("Task 3")

while not queue.is_empty():
    print("Processing:", queue.dequeue())



def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev








