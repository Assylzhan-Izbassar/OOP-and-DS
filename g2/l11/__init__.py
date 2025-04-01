class MaxHeap:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self.heap[parent] >= self.heap[idx]:
                break

            # self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]

            temp = self.heap[idx]
            self.heap[idx] = self.heap[parent]
            self.heap[parent] = temp

            idx = parent

    def _heapify_down(self, idx):
        size = len(self.heap)
        while idx < size:
            left = 2 * idx + 1
            right = 2 * idx + 2

            smallest = idx

            if left < size and self.heap[left] > self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] > self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break

            temp = self.heap[idx]
            self.heap[idx] = self.heap[smallest]
            self.heap[smallest] = temp

            idx = smallest

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_root(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def heap_sort(self):
        temp = self.heap
        result = []

        while len(self.heap) > 0:
            result.append(self.extract_root())

        self.heap = temp
        return result


def print_heap(heap):
    for x in heap:
        print(x, end=' ')
    print()

heap = MaxHeap()
heap.insert(1)
heap.insert(12)
heap.insert(10)
heap.insert(9)

# root = heap.extract_root()
# print(root)
print_heap(heap.heap)

sorted_heap = heap.heap_sort()
print_heap(sorted_heap)