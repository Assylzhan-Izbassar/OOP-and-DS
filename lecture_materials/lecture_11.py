

import heapq

heap = []
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print(heapq.heappop(heap))  # 5


import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Преобразуем в кучу
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

arr = [5, 3, 8, 1, 2]
print(heap_sort(arr))  # [1, 2, 3, 5, 8]





class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            # Меняем местами
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)




    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < size and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < size and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
            if smallest == index:
                break

            # Меняем местами
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root




    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


heap = MinHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
print(heap.heap)  # [5, 20, 10]
