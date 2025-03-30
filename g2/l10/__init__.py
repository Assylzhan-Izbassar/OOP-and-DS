import time

def merge(left, right):
    result = []
    i, j = 0, 0

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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) - 1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

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


li = [4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,
      4, 1, 2, 6, 7, 5,]

start = time.time()
bubble_sort(li)
end = time.time()

print('bubble sort', end - start)



start = time.time()
bubble_sort_2(li)
end = time.time()

print('optimized bubble sort', end - start)

start = time.time()
merge_sort(li)
end = time.time()

print('merge sort', end - start)

start = time.time()
quick_sort(li)
end = time.time()

print('quick_sort', end - start)


# g = [1, 2, 3]
# s = [1, 1, 2, 5]
#
# bubble_sort_2(g)
# bubble_sort_2(s)
#
# # min_len = min(len(g), len(s))
# child = 0
# cookie = 0
#
# while child < len(g) and cookie < len(s):
#     if g[child] <= s[cookie]:
#         child += 1
#     cookie += 1
#
# # for i in range(min_len):
# #     if s[i] >= g[i]:
# #         child += 1
#
# print(child)


