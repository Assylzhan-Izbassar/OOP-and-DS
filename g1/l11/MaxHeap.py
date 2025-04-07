class MaxHeap:
    def __init__(self):
        self.heap = []

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def preorder(self, i):
        if i >= len(self.heap):
            return
        print(self.heap[i])
        self.preorder(self.left(i))
        self.preorder(self.right(i))

    def inorder(self, i=0):
        if i >= len(self.heap):
            return
        self.inorder(self.left(i))
        print(self.heap[i])
        self.inorder(self.right(i))

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self.heap[idx] <= self.heap[parent]:
                break

            temp = self.heap[idx]
            self.heap[idx] = self.heap[parent]
            self.heap[parent] = temp

            idx = parent

    def insert(self, new_value):
        self.heap.append(new_value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_down(self, idx):
        size = len(self.heap)

        while idx < size:
            left = self.left(idx)
            right = self.right(idx)
            maxi_idx = idx

            if left < size and self.heap[left] > self.heap[maxi_idx]:
                maxi_idx = left
            if right < size and self.heap[right] > self.heap[maxi_idx]:
                maxi_idx = right
            if maxi_idx == idx:
                break

            temp = self.heap[idx]
            self.heap[idx] = self.heap[maxi_idx]
            self.heap[maxi_idx] = temp

            idx = maxi_idx

    def extract_top(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def linear_search(self, value):
        for i in range(len(self.heap)):
            if self.heap[i] == value:
                return i
        return -1

    def delete_elem(self, elem):
        res_idx = self.linear_search(elem)

        if res_idx == -1:
            return None

        # current = self.heap[res_idx]
        self.heap[res_idx] = self.heap.pop()
        self._heapify_down(res_idx)

        return elem

    def heap_sort(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap

        temp = self.heap.copy()

        result = []
        size = len(self.heap)

        while size > 0:
            result.append(self.extract_top())
            size -= 1

        self.heap = temp
        return result

heap = MaxHeap()
heap.insert(6)
heap.insert(3)
heap.insert(4)
heap.insert(2)
heap.insert(5)
heap.insert(1)
heap.insert(8)
heap.insert(9)
heap.insert(12)


for x in heap.heap:
    print(x, end=' ')

print()
heap.preorder(0)

# print('Top', heap.extract_top())
#
# for x in heap.heap:
#     print(x, end=' ')
#
# print()
# heap.preorder(0)


# print('Deleted', heap.delete_elem(9))
#
# for x in heap.heap:
#     print(x, end=' ')
#
# print()
# heap.preorder(0)

print('Heap Sort')
for x in heap.heap_sort():
    print(x, end=' ')
print()