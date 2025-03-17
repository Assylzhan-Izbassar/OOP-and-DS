class Queue:
    def __init__(self, size=100):
        self.items = [None] * size
        self.size = size
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            print('Очередь заполнен')
            return None
        self.items[self.count] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print('Очередь пустая')
            return None
        item = self.items.pop(0)
        self.items.append(None)
        self.count -= 1
        return item

    def front(self):
        if self.is_empty():
            print('Очередь пустая')
            return None
        return self.items[0]

    def display(self):
        for item in self.items:
            print(item, end=' ')

queue = Queue(10)
queue.enqueue('M')
queue.enqueue('W')
queue.enqueue('W')
queue.enqueue('M')
queue.enqueue('M')

while not queue.is_empty():
    item = queue.dequeue()
    if item is not None:
        print('Обслуживаем ' + item)

queue.display()