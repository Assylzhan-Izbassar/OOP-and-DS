
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
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


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)






def bubble_sort(arr):
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

li = [1, 5, 3, 43, 21, 4]
print(quick_sort(li))


g = [1, 2, 3] # children's demand
s = [1, 1] # available cookies





def findContentChildren(g, s):
    bubble_sort(g)
    bubble_sort(s)

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:  # If the cookie satisfies the child
            child += 1  # We give cookies to the child
        cookie += 1

    return child




# Тест
print(findContentChildren([1, 2, 3], [1, 1]))  # Вывод: 1
print(findContentChildren([1, 2], [1, 2, 3]))  # Вывод: 2






