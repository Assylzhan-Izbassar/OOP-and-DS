import time

def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


li = [4, 7, 2, 1, 43, 65, 20]


start = time.time()
print(bubble_sort(li))
end = time.time()
print('bubble sort', end - start)

start = time.time()
print(bubble_sort_2(li))
end = time.time()
print('bubble sort optimized', end - start)