def print_heap(heap):
    for x in heap:
        print(x, end=' ')
    print()

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def swap(self, parent, idx):
        temp = self.heap[parent]
        self.heap[parent] = self.heap[idx]
        self.heap[idx] = temp

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            # Основное условие
            if self.heap[parent] >= self.heap[idx]:
                break

            self.swap(parent, idx)

            idx = parent

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)

    def _heapify_down(self, idx):
        while idx < self.size:
            left = 2 * idx + 1
            right = 2 * idx + 2

            smallest = idx

            if left < self.size and self.heap[left] > self.heap[smallest]:
                smallest = left
            if right < self.size and self.heap[right] > self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break

            self.swap(idx, smallest)

            idx = smallest

    def extract_top(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self._heapify_down(0)
        return root

heap = MaxHeap()
heap.insert(1)
heap.insert(16)
heap.insert(3)
heap.insert(9)
heap.insert(23)

print_heap(heap.heap)

print(heap.extract_top())

print_heap(heap.heap)