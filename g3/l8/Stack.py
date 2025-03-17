class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def display_1(self):
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i])

    def display_2(self):
        temp = self.items.copy()
        while self.is_empty() is False:
            print(self.peek())
            self.pop()
        self.items = temp


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display_2()
print(stack.is_empty())



# Task 1
# ()(({}(())))()

brackets = '()(((())))())('
n = len(brackets)
marker = [0] * n

for i in range(n):
    b = brackets[i]
    if b == '(' and marker[i] == 0:
        for j in range(i + 1, n):
            b2 = brackets[j]
            if b2 == ')' and marker[j] == 0:
                marker[i] = 1
                marker[j] = 1
                break
prod = 1

for i in range(n):
    prod *= marker[i]

if prod == 1:
    print('Valid')
else:
    print('Invalid')


checker = Stack()

for bracket in brackets:
    if bracket == '(':
        checker.push('(')
    elif bracket == ')':
        checker.pop()

if checker.is_empty() is True:
    print('Valid')
else:
    print('Invalid')
    checker.display_2()



# tracker = []

# for i in range(0, n):
#     if brackets[i] == '(' or brackets[i] == '{':
#         tracker.append(i)





class Queue:
    def __init__(self, size):
        self.items = [None] * size
        self.count = 0
        self.capacity = size

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full')
            return None
        self.items[self.count] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return None
        for i in range(1, self.count):
            self.items[i - 1] = self.items[i]
        self.items[self.count] = None
        self.count -= 1

    def display(self):
        for i in range(0, self.count):
            print(self.items[i], end=' ')


queue = Queue(10)
queue.enqueue('M')
queue.enqueue('W')
queue.enqueue('W')
queue.enqueue('M')
queue.enqueue('M')

queue.dequeue()
queue.dequeue()

queue.display()




