import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def bubble_sort_opt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

arr = [43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100
       ]

start = time.time()
bubble_sort(arr)
end = time.time()

for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print(end - start)

arr = [43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100
       ]

start = time.time()
bubble_sort_opt(arr)
end = time.time()

for i in range(len(arr)):
    print(arr[i], end=' ')

print()
print(end - start)

arr = [43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
        43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100
       ]

start = time.time()
result = merge_sort(arr)
end = time.time()

for i in range(len(result)):
    print(result[i], end=' ')

print()
print(end - start)


arr = [43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
        43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100,
       43, 21, 54, 2, 4, 86, 100
       ]

start = time.time()
result = quick_sort(arr)
end = time.time()

for i in range(len(result)):
    print(result[i], end=' ')

print()
print(end - start)

print(len(result))

